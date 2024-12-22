let btn = document.querySelector('.header__notification');
let notify = document.querySelector('.header__notify');

btn.addEventListener('click', () => {
	if (btn.classList.contains('active')) {
		notify.classList.toggle('active');
	}
});

document.body.addEventListener('click', (e) => {
	if (e.target.classList.contains('notify__img') || e.target.classList.contains('notify')) {
		// Do nothing
	} else if (e.target.classList.contains('notify__text') || e.target.classList.contains('header__notification')) {
		notify.classList.toggle('active');
	} else {
		notify.classList.remove('active');
	}
});