const input = document.getElementById('pdf_file');
const zone = document.getElementById('dropZone');
const title = document.getElementById('fileTitle');
const hint = document.getElementById('fileHint');
if (input) {
  input.addEventListener('change', () => showFile(input.files[0]));
  function showFile(file) {
    if (!file) return;
    title.textContent = file.name;
    hint.textContent = `${(file.size / 1024 / 1024).toFixed(2)} MB · Ready to upload`;
  }
  ['dragenter', 'dragover'].forEach(name => zone.addEventListener(name, e => { e.preventDefault(); zone.classList.add('dragging'); }));
  ['dragleave', 'drop'].forEach(name => zone.addEventListener(name, e => { e.preventDefault(); zone.classList.remove('dragging'); }));
  zone.addEventListener('drop', e => {
    const file = e.dataTransfer.files[0];
    if (file && file.name.toLowerCase().endsWith('.pdf')) {
      const transfer = new DataTransfer(); transfer.items.add(file); input.files = transfer.files; showFile(file);
    } else if (file) { title.textContent = 'Please choose a PDF file'; hint.textContent = 'Only .pdf files are accepted'; }
  });
  document.getElementById('uploadForm').addEventListener('submit', () => {
    const button = document.querySelector('.primary-button');
    button.querySelector('span').textContent = 'Extracting…'; button.disabled = true;
  });
}
