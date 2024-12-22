let swiperWeather = new Swiper('.weather__swiper', {
	// Optional parameters
	direction: 'horizontal',
	// loop: true,

	spaceBetween: 10,

	// If we need pagination
	pagination: {
		el: '.swiper-pagination',
	},
});

let swiperTrack = new Swiper('.track__swiper', {
	// Optional parameters
	direction: 'horizontal',
	loop: true,

	spaceBetween: 10,

	// If we need pagination
	pagination: {
		el: '.track-paggination',
	},
});

// Погода
function setWeatherEqualHeight() {
	const weather = document.querySelectorAll('.weather__card');
	let maxHeight = 0;

	// Сброс высоты для вычисления
	weather.forEach(w => {
		w.style.height = 'auto';
	});

	// Находим максимальную высоту
	weather.forEach(w => {
		maxHeight = Math.max(maxHeight, w.offsetHeight);
	});

	// Устанавливаем одинаковую высоту
	weather.forEach(w => {
		w.style.height = `${maxHeight}px`;
	});
}

// Вызываем функцию после загрузки страницы и при изменении размеров окна
window.addEventListener('load', setWeatherEqualHeight);
window.addEventListener('resize', setWeatherEqualHeight);

// Треки
function setTrackEqualHeight() {
	const tracks = document.querySelectorAll('.track');
	let maxHeight = 0;

	// Сброс высоты для вычисления
	tracks.forEach(track => {
		track.style.height = 'auto';
	});

	// Находим максимальную высоту
	tracks.forEach(track => {
		maxHeight = Math.max(maxHeight, track.offsetHeight);
	});

	// Устанавливаем одинаковую высоту
	tracks.forEach(track => {
		track.style.height = `${maxHeight}px`;
	});
}

// Вызываем функцию после загрузки страницы и при изменении размеров окна
window.addEventListener('load', setTrackEqualHeight);
window.addEventListener('resize', setTrackEqualHeight);