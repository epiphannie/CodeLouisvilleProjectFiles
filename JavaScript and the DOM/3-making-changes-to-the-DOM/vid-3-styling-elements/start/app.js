const toggleList = document.getElementById('toggleList');
const listDiv = document.querySelector('.list');
const input = document.querySelector('input.description');
const p = document.querySelector('p.description');
const button = document.querySelector('button.description');

toggleList.addEventListener('click', () => {
  if (listDiv.style.display == 'none') {
    toggleList.textContent = 'Hide List';
    listDiv.style.display='block';
  } else {
    listDiv.style.display='none';
    toggleList.textContent = 'Show List';
  }
});

button.addEventListener('click', () => {
  p.innerHTML = input.value + ':';
});
