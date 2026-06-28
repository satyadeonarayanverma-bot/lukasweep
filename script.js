// script.js - Premium Modern Tribute Page

// Seeding Default Comments
const defaultComments = [
  { name: "A Grateful Friend", msg: "Aqsa, your kindness is inspiring. Thank you for making a difference and saving Lukas!", date: "6/25/2026" },
  { name: "Family of Lukas", msg: "We are forever grateful for your immense generosity. You gave Lukas a second chance at life. Thank you from the bottom of our hearts.", date: "6/26/2026" },
  { name: "Medical Staff", msg: "Financial donations like yours make life-saving treatments possible. Thank you for helping Lukas. You are a true hero.", date: "6/27/2026" },
  { name: "Cancer Care Society", msg: "Your selfless act of support is a beacon of hope for everyone facing these high medical costs. Thank you, Aqsa.", date: "6/28/2026" }
];

document.addEventListener('DOMContentLoaded', () => {
  setupGuestbook();
  setupSparkleEvents();
  
  // Start subtle periodic background sparkles
  setInterval(spawnBackgroundSparkle, 2000);
});

// ================= GUESTBOOK SYSTEM =================

function setupGuestbook() {
  const form = document.getElementById('guestbook-form');
  if (!form) return;

  // Initialize comments storage if empty
  let comments = localStorage.getItem('aqsa_final_comments');
  if (!comments) {
    comments = JSON.stringify(defaultComments);
    localStorage.setItem('aqsa_final_comments', comments);
  }

  renderComments();

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const nameInput = document.getElementById('input-name');
    const msgInput = document.getElementById('input-msg');

    if (nameInput && msgInput) {
      const name = nameInput.value.trim();
      const msg = msgInput.value.trim();

      if (name && msg) {
        const newComment = {
          name: name,
          msg: msg,
          date: new Date().toLocaleDateString()
        };

        const stored = JSON.parse(localStorage.getItem('aqsa_final_comments') || '[]');
        stored.push(newComment);
        localStorage.setItem('aqsa_final_comments', JSON.stringify(stored));

        nameInput.value = '';
        msgInput.value = '';

        renderComments();

        // Scroll to the bottom of the comments list
        const container = document.getElementById('comments-container');
        if (container) {
          container.scrollTop = container.scrollHeight;
        }
      }
    }
  });
}

function renderComments() {
  const container = document.getElementById('comments-container');
  if (!container) return;

  const comments = JSON.parse(localStorage.getItem('aqsa_final_comments') || '[]');
  container.innerHTML = '';

  comments.forEach(c => {
    const entry = document.createElement('div');
    entry.className = 'guestbook-entry';
    entry.innerHTML = `
      <div class="entry-header">
        <span class="entry-author">${escapeHTML(c.name)}</span>
        <span class="entry-date">${escapeHTML(c.date)}</span>
      </div>
      <div class="entry-msg">${escapeHTML(c.msg)}</div>
    `;
    container.appendChild(entry);
  });
}

function escapeHTML(str) {
  return str.replace(/[&<>'"]/g, 
    tag => ({
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      "'": '&#39;',
      '"': '&quot;'
    }[tag] || tag)
  );
}

// ================= ELEGANT GOLD SPARKLES CONTROLLER =================

function setupSparkleEvents() {
  const btn = document.getElementById('sparkle-btn');
  if (btn) {
    btn.addEventListener('click', (e) => {
      // Get click position relative to screen for origin
      const rect = btn.getBoundingClientRect();
      const x = rect.left + rect.width / 2;
      const y = rect.top + rect.height / 2;
      
      triggerSparkles(x, y);
    });
  }
}

function triggerSparkles(originX, originY) {
  const container = document.getElementById('sparkle-container');
  if (!container) return;

  const sparkleCount = 20;

  for (let i = 0; i < sparkleCount; i++) {
    const dot = document.createElement('div');
    dot.className = 'sparkle-dot';
    
    // Set custom coordinates near origin
    const offsetX = (Math.random() - 0.5) * 120;
    const offsetY = (Math.random() - 0.5) * 40;
    dot.style.left = `${originX + offsetX}px`;
    dot.style.top = `${originY + offsetY}px`;
    
    // Set animations parameters
    const scale = Math.random() * 1 + 0.5; // 0.5 to 1.5
    const duration = Math.random() * 1.5 + 1.5; // 1.5s to 3s
    const delay = Math.random() * 0.2;
    
    dot.style.transform = `scale(${scale})`;
    dot.style.animationDuration = `${duration}s`;
    dot.style.animationDelay = `${delay}s`;
    
    // Set random slight variations in gold color
    const goldVariations = ['#C5A880', '#E5C494', '#D4AF37', '#F3E5AB'];
    dot.style.backgroundColor = goldVariations[Math.floor(Math.random() * goldVariations.length)];
    
    // Subtle shadow box
    dot.style.boxShadow = `0 0 10px ${dot.style.backgroundColor}`;

    container.appendChild(dot);

    dot.addEventListener('animationend', () => {
      dot.remove();
    });
  }
}

function spawnBackgroundSparkle() {
  const container = document.getElementById('sparkle-container');
  if (!container) return;

  const dot = document.createElement('div');
  dot.className = 'sparkle-dot';
  
  // Spawn randomly at bottom/middle of screen
  const x = Math.random() * window.innerWidth;
  const y = window.innerHeight * 0.8 + Math.random() * (window.innerHeight * 0.15);
  
  dot.style.left = `${x}px`;
  dot.style.top = `${y}px`;
  
  const scale = Math.random() * 0.6 + 0.3; // smaller background dots
  const duration = Math.random() * 2 + 2.5; // slow rise
  
  dot.style.transform = `scale(${scale})`;
  dot.style.animationDuration = `${duration}s`;
  
  const goldVariations = ['#C5A880', '#F3E5AB', '#FFF8DC'];
  dot.style.backgroundColor = goldVariations[Math.floor(Math.random() * goldVariations.length)];
  
  container.appendChild(dot);

  dot.addEventListener('animationend', () => {
    dot.remove();
  });
}
