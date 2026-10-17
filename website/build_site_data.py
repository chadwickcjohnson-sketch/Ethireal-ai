from pathlib import Path
import json
import os
import argparse
from datetime import datetime
from typing import Dict, Any, List

DEFAULT_INCLUDE_FULL = os.environ.get("PUBLISH_FULL_DOCUMENTS", "false").lower() in ("1", "true", "yes")
DEFAULT_OUTPUT_DIR = Path(os.environ.get("SITE_OUTPUT_DIR", "website/data"))


def parse_ts(value: str):
    if not value:
        return datetime.min
    try:
        # Accept ISO 8601 with or without Z
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except Exception:
        try:
            return datetime.utcfromtimestamp(float(value))
        except Exception:
            return datetime.min


def redact_content(content: Dict[str, Any]) -> Dict[str, Any]:
    # Basic redaction: remove keys that look like PII
    if not isinstance(content, dict):
        return {}
    redacted = {}
    pii_keys = {"ssn", "ssn_last4", "dob", "birthdate", "email", "phone", "address", "ssn_full", "tax_id"}
    for k, v in content.items():
        if k.lower() in pii_keys:
            redacted[k] = "REDACTED"
        else:
            # For nested dicts, shallow redact recursively for safety
            if isinstance(v, dict):
                redacted[k] = redact_content(v)
            else:
                redacted[k] = v
    return redacted


def collect_documents(root: Path, include_full: bool = False) -> List[Dict[str, Any]]:
    docs_dir = root / "features" / "copilot" / "plans"
    results = []

    if not docs_dir.exists():
        return results

    for path in sorted(docs_dir.glob("*.json")):
        try:
            with path.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
        except Exception:
            continue

        entry = {
            "doc_type": data.get("doc_type") or data.get("type") or path.stem,
            "title": data.get("title") or path.stem,
            "timestamp": data.get("timestamp") or data.get("created_at") or data.get("time") or None,
            "updated_at": data.get("updated_at"),
            "sha256_signature": (data.get("sha256_signature") or data.get("sha256") or "")[:64],
            "status": data.get("status") or "",
            "source_file": path.name,
            "download_url": f"/legal/{path.name}",
        }

        if include_full:
            entry["content"] = data.get("content")
        else:
            entry["content"] = redact_content(data.get("content", {}))

        results.append(entry)

    # Sort newest first by timestamp, fallback to filename/time
    results.sort(key=lambda d: parse_ts(d.get("timestamp") or ""), reverse=True)
    return results


def build_site_metadata(root: Path, output_dir: Path, include_full: bool = DEFAULT_INCLUDE_FULL) -> Path:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    docs = collect_documents(root, include_full=include_full)

    payload = {"generated_at": datetime.utcnow().isoformat() + "Z", "documents": docs}
    out_file = output_dir / "legal_documents.json"
    with out_file.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)

    return out_file


def main():
    parser = argparse.ArgumentParser(description="Build public legal metadata for the website.")
    parser.add_argument("--output", "-o", default=str(DEFAULT_OUTPUT_DIR), help="Output directory for generated site data")
    parser.add_argument("--include-full", action="store_true", help="Include full document contents in the public export (review privacy implications)")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    include = args.include_full or DEFAULT_INCLUDE_FULL
    out = build_site_metadata(root, Path(args.output), include_full=include)
    print(f"Wrote public metadata to: {out}")


if __name__ == "__main__":
    main()
