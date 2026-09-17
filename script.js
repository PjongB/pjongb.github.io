'use strict';
document.querySelector('.print-button').addEventListener('click', () => window.print());
const links = [...document.querySelectorAll('.project-nav a')];
const projects = [...document.querySelectorAll('.project')];
let pending = false;
function updateNavigation() {
  const boundary = window.innerHeight * 0.35;
  let current = projects[0];
  for (const project of projects) {
    if (project.getBoundingClientRect().top <= boundary) current = project;
  }
  for (const link of links) {
    const active = link.hash === '#' + current.id;
    link.classList.toggle('active', active);
    if (active) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  }
  pending = false;
}
window.addEventListener('scroll', () => {
  if (!pending) { pending = true; requestAnimationFrame(updateNavigation); }
}, { passive: true });
window.addEventListener('resize', updateNavigation);
updateNavigation();
