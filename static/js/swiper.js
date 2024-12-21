let swiperWeather = new Swiper('.weather__swiper', {
	// Optional parameters
	direction: 'horizontal',
	// loop: true,

	// If we need pagination
	pagination: {
		el: '.swiper-pagination',
	},
});

let swiperTrack = new Swiper('.track__swiper', {
	// Optional parameters
	direction: 'horizontal',
	loop: true,

	// If we need pagination
	pagination: {
		el: '.track-paggination',
	},
});