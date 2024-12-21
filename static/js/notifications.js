let btn = document.querySelector('.header__notification');
let notify = document.querySelector('.header__notify');

btn.addEventListener('click', () => {
	if (btn.classList.contains('active')) {
		notify.classList.toggle('active');
	}
});