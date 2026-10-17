document.addEventListener('DOMContentLoaded', () => {
  const buttons = document.querySelectorAll('.checkout-btn');

  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      const url = button.dataset.checkoutUrl;
      if (!url) return;

      if (url.startsWith('http')) {
        window.open(url, '_blank', 'noopener,noreferrer');
      } else {
        window.location.href = url;
      }
    });
  });
});
