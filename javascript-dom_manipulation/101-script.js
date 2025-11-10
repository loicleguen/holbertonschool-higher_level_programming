document.addEventListener('DOMContentLoaded', function () {
  const btn = document.querySelector('#btn_translate');
  const select = document.querySelector('#language_code');
  const output = document.querySelector('#hello');

  btn.addEventListener('click', function () {
    const lang = select.value;
    if (lang) {
      fetch(`https://hellosalut.stefanbohacek.com/?lang=${lang}`)
        .then(response => response.json())
        .then(data => {
          output.textContent = data.hello;
        });
    } else {
      output.textContent = '';
    }
  });
});
