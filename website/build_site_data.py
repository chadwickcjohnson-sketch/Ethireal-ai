from pathlib import Path
import json
import os

def build_site_metadata(root: Path, output_dir: Path, include_full: bool = False):
    """Collect generated legal document metadata into a site-ready JSON file."""
    docs_dir = root / "features" / "copilot" / "plans"
    output_dir.mkdir(parents=True, exist_ok=True)
    entries = []

    if docs_dir.exists():
        for path in sorted(docs_dir.glob("*.json")):
            try:
                with path.open("r", encoding="utf-8") as handle:
                    data = json.load(handle)
            except json.JSONDecodeError:
                continue

            public_entry = {
                "doc_type": data.get("doc_type"),
                "title": data.get("title"),
                "timestamp": data.get("timestamp"),
                "sha256_signature": data.get("sha256_signature", "")[:16] + "...",
                "status": data.get("status"),
                "download_url": f"/legal/{path.name}",
            }
            if include_full:
                public_entry["content"] = data.get("content", {})
            entries.append(public_entry)

    payload = {"documents": entries}
    out_file = output_dir / "legal_documents.json"
    with out_file.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)

    return out_file


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    out = root / "website" / "data"
    build_site_metadata(root, out, include_full=False)
