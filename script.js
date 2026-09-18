'use strict';
document.querySelector('.print-button')?.addEventListener('click', async () => {
  const button = document.querySelector('.print-button');
  button.disabled = true;
  try {
    await Promise.allSettled([
      document.fonts?.ready,
      ...Array.from(document.images, image => image.decode())
    ]);
    window.print();
  } finally {
    button.disabled = false;
  }
});
