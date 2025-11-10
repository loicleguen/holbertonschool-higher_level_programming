document.addEventListener('DOMContentLoaded', function () {
  const ul = document.querySelector('.my_list');
  const AddItem = document.querySelector('#add_item');
  const RemoveItem = document.querySelector('#remove_item');
  const ClearList = document.querySelector('#clear_list');

  AddItem.addEventListener('click', function () {
    const li = document.createElement('li');
    li.textContent = 'Item';
    ul.appendChild(li);
  });

  RemoveItem.addEventListener('click', function () {
    if (ul.lastElementChild) {
      ul.removeChild(ul.lastElementChild);
    }
  });

  ClearList.addEventListener('click', function () {
    ul.innerHTML = '';
  });
});
