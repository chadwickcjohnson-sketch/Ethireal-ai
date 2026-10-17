async function loadLegalDocs() {
  const container = document.getElementById('legal-doc-list');
  if (!container) return;

  try {
    const res = await fetch('data/legal_documents.json');
    const payload = await res.json();
    const docs = payload.documents || [];

    if (!docs.length) {
      container.innerHTML = '<div class="card"><p>No legal documents are currently available.</p></div>';
      return;
    }

    container.innerHTML = docs.map(doc => `
      <article class="doc-item">
        <h3>${doc.title || doc.doc_type}</h3>
        <small>${doc.doc_type} • ${doc.timestamp || 'n/a'} • SHA-256: ${doc.sha256_signature || 'n/a'}</small>
        <p><a href="${doc.download_url}">View metadata</a></p>
      </article>
    `).join('');
  } catch (error) {
    container.innerHTML = '<div class="card"><p>Legal data is unavailable right now.</p></div>';
  }
}

loadLegalDocs();
