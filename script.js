// ===================================================
// 1,000,000 Repetitions Ultra-Responsive Stream
// Fixed Typos & Zero-Lag On-Demand Infinite Scroll
//
// Lines:
// 1. EAT WELL
// 2. STAY HYDRATED
// 3. TAKE MEDS ON TIME
// 4. YOUR ADI IS ALWAYS HERE FOR YOU TO HELP
// ===================================================

const PHRASE_BLOCK = "EAT WELL\nSTAY HYDRATED\nTAKE MEDS ON TIME\nYOUR ADI IS ALWAYS HERE FOR YOU TO HELP\n";
const TOTAL_REPETITIONS = 1000000;
const INITIAL_REPETITIONS = 300;
const BATCH_REPETITIONS = 200;

let currentCount = 0;

document.addEventListener('DOMContentLoaded', () => {
  renderWatermarkBg();
  setupLoveModal();
  
  const container = document.getElementById('spam-track');
  if (!container) return;

  // Render initial batch for instant page load
  appendChunk(container, INITIAL_REPETITIONS);

  // On-demand scroll listener (Appends lines as user scrolls)
  let isAppending = false;
  window.addEventListener('scroll', () => {
    if (isAppending || currentCount >= TOTAL_REPETITIONS) return;

    // Trigger when 1200px from bottom
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 1200) {
      isAppending = true;
      requestAnimationFrame(() => {
        appendChunk(container, BATCH_REPETITIONS);
        isAppending = false;
      });
    }
  }, { passive: true });
});

function appendChunk(container, countToAppend) {
  if (currentCount >= TOTAL_REPETITIONS) return;

  const actualCount = Math.min(countToAppend, TOTAL_REPETITIONS - currentCount);
  const blockDiv = document.createElement('div');
  blockDiv.className = 'text-chunk-block';
  blockDiv.textContent = PHRASE_BLOCK.repeat(actualCount);

  container.appendChild(blockDiv);
  currentCount += actualCount;
}

// Render Background Tiled Watermark Layer ("aqsaaww ilysm" + Mini Photo Tiles)
function renderWatermarkBg() {
  const container = document.getElementById('watermark-container');
  if (!container) return;

  const rowsCount = 28;
  const itemsPerRow = 12;
  const photoSrc = "WhatsApp Image 2026-07-26 at 17.02.03.jpeg";

  const fragment = document.createDocumentFragment();

  for (let r = 0; r < rowsCount; r++) {
    const row = document.createElement('div');
    row.className = 'watermark-row';

    let rowContent = '';
    for (let i = 0; i < itemsPerRow; i++) {
      rowContent += `
        <span>aqsaaww ilysm 💖</span>
        <img src="${photoSrc}" class="watermark-photo-item" alt="watermark">
      `;
    }

    row.innerHTML = rowContent + rowContent;
    fragment.appendChild(row);
  }

  container.appendChild(fragment);
}

// Interactive Love Message Modal Setup
function setupLoveModal() {
  const careBtn = document.getElementById('care-btn');
  const modal = document.getElementById('love-modal');
  const closeBtn = document.getElementById('close-modal-btn');

  if (!careBtn || !modal || !closeBtn) return;

  careBtn.addEventListener('click', () => {
    modal.classList.add('active');
  });

  closeBtn.addEventListener('click', () => {
    modal.classList.remove('active');
  });

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.classList.remove('active');
    }
  });
}
