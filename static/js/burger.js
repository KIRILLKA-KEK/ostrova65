let burger = document.querySelector('.header__burger');
let menu = document.querySelector('.menu');

burger.addEventListener('click', () => {
	burger.classList.toggle('active');
	menu.classList.toggle('active');
});