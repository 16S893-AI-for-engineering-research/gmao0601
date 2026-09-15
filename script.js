// Easter egg: hovering over "sailing" sends a sailboat sailing across the screen.
document.addEventListener('DOMContentLoaded', () => {
  const trigger = document.getElementById('sail-trigger');
  if (!trigger) return;

  let cooldown = false;
  const BOAT_COUNT = 18;

  trigger.addEventListener('mouseenter', () => {
    if (cooldown) return;
    cooldown = true;

    let remaining = BOAT_COUNT;

    for (let i = 0; i < BOAT_COUNT; i++) {
      const boat = document.createElement('div');
      boat.className = 'sailboat';
      boat.textContent = '⛵';

      // Stagger start times and vary height/speed/size a bit for a fleet effect.
      const delay = i * 0.25; // seconds between each boat's launch
      const duration = 3.5 + Math.random() * 2; // 3.5s - 5.5s
      const bottom = 10 + Math.random() * 60; // px from bottom, varied "lanes"
      const scale = 0.7 + Math.random() * 0.6; // size variation

      boat.style.bottom = `${bottom}px`;
      boat.style.fontSize = `${3 * scale}rem`;
      boat.style.animationDuration = `${duration}s`;
      boat.style.animationDelay = `${delay}s`;

      document.body.appendChild(boat);

      boat.addEventListener('animationend', () => {
        boat.remove();
        remaining -= 1;
        if (remaining <= 0) cooldown = false;
      });
    }
  });
});

// Easter egg: hovering over "Coming soon..." on the Project page spawns
// a bunch of question marks popping up across the screen.
document.addEventListener('DOMContentLoaded', () => {
  const comingSoon = document.getElementById('coming-soon');
  if (!comingSoon) return;

  let intervalId = null;

  function spawnQuestionMark() {
    const mark = document.createElement('div');
    mark.className = 'question-mark';
    mark.textContent = '?';

    const left = Math.random() * 100; // vw
    const top = Math.random() * 100; // vh
    const size = 1.5 + Math.random() * 2.5; // rem
    const hue = Math.floor(Math.random() * 360);

    mark.style.left = `${left}vw`;
    mark.style.top = `${top}vh`;
    mark.style.fontSize = `${size}rem`;
    mark.style.color = `hsl(${hue}, 70%, 45%)`;

    document.body.appendChild(mark);

    mark.addEventListener('animationend', () => {
      mark.remove();
    });
  }

  comingSoon.addEventListener('mouseenter', () => {
    if (intervalId) return;
    spawnQuestionMark();
    intervalId = setInterval(spawnQuestionMark, 100);
  });

  comingSoon.addEventListener('mouseleave', () => {
    if (intervalId) {
      clearInterval(intervalId);
      intervalId = null;
    }
  });
});

// Dev Log page: scramble/decode text on load, hacker-movie style.
document.addEventListener('DOMContentLoaded', () => {
  const targets = document.querySelectorAll('[data-text]');
  if (!targets.length) return;

  const chars = '!<>-_\\/[]{}—=+*^?#________';
  const revealDelayPerChar = 80; // ms between each character locking in
  const scrambleSpeed = 40; // ms between scramble frames

  function randomChar() {
    return chars[Math.floor(Math.random() * chars.length)];
  }

  function scrambleElement(el) {
    const finalText = el.dataset.text || el.textContent;
    let frame = 0;
    let revealed = 0;

    const interval = setInterval(() => {
      frame++;
      let output = '';

      for (let i = 0; i < finalText.length; i++) {
        if (i < revealed) {
          output += finalText[i];
        } else if (finalText[i] === ' ') {
          output += ' ';
        } else {
          output += randomChar();
        }
      }

      el.textContent = output;

      if (frame % Math.max(1, Math.round(revealDelayPerChar / scrambleSpeed)) === 0) {
        revealed++;
      }

      if (revealed > finalText.length) {
        clearInterval(interval);
        el.textContent = finalText;
      }
    }, scrambleSpeed);
  }

  targets.forEach(scrambleElement);
});

// Dev Log page: clicking an entry's title expands/collapses its body text.
document.addEventListener('DOMContentLoaded', () => {
  const toggles = document.querySelectorAll('.log-toggle');
  if (!toggles.length) return;

  toggles.forEach((toggle) => {
    const body = toggle.nextElementSibling;
    if (!body) return;

    function toggleEntry() {
      const collapsed = body.classList.toggle('collapsed');
      toggle.setAttribute('aria-expanded', String(!collapsed));
    }

    toggle.addEventListener('click', toggleEntry);
    toggle.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        toggleEntry();
      }
    });
  });
});
