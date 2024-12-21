// justimifyo@gufum.com
// 12wq34re56yt78iu

maptilersdk.config.apiKey = 'ZHCUQSwtx24Zgsm2wgEG';
const map = new maptilersdk.Map({
	container: 'map', // container's id or the HTML element to render the map
	// style: maptilersdk.MapStyle.OUTDOOR,
	style: 'winter-v2',
	// center: [142.793306, 46.953702], // starting position [lng, lat]
	center: [142.781389, 46.955707],
	zoom: 13, // starting zoom
	terrain: true,
	terrainControl: true,
	pitch: 80,
	bearing: 70.86,
	// maxPitch: 85,
	maxZoom: 14
});

let el1 = document.querySelector('.maplibregl-ctrl-top-right');
let el2 = document.querySelector('.maplibregl-ctrl-bottom-right');
let el3 = document.querySelector('.maplibregl-ctrl-bottom-left');
el1.remove(); el2.remove(); el3.remove();