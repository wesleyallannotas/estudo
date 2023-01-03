const buttonOpenModal = document.getElementById('openModal');
const modal = document.getElementById('modal');
const body = document.querySelector('body');

buttonOpenModal.onclick = () => {
  modal.classList.remove('invisible');
};

body.addEventListener('keydown', e => {
  let isEscKey = e.key === 'Escape';
  let isModalOpen = !modal.classList.value.includes('invisible');
  if (isEscKey && isModalOpen) {
    modal.classList.add('invisible');
  }
});
