startFilter = document.getElementById("start-filter");
endFilter = document.getElementById("end-filter");
startThumb = document.getElementById("start-thumb");
endThumb = document.getElementById("end-thumb");
backgroundLeft = document.getElementById("background-left");
backgroundRight = document.getElementById("background-right");
endThumb = document.getElementById("end-thumb");

range = document.getElementById("range");
startFilter.addEventListener(
    "input",
    (ev) => {
        value = Math.max(0, Math.min(ev.target.value, endFilter.value));
        ev.target.value = value;
        range.style.left = value + "%";
        startThumb.style.left = value + "%";
    },
    true
);
endFilter.addEventListener(
    "input",
    (ev) => {
        value = Math.min(100, Math.max(ev.target.value, startFilter.value));
        ev.target.value = value;
        console.log(ev.target.value);
        range.style.right = 100 - value + "%";
        endThumb.style.right = 100 - value + "%";
    },
    true
);

// select the canvas element created in the html.
const map = document.getElementById("canvas-map");
const points = document.getElementById("canvas-points")

// Actual width and height. No idea if clienWidth would be a better option..?
const width = map.offsetWidth;
const height = map.offsetHeight;

// Set a projection for the map. Projection = transform a lat/long on a position on the 2d map.
const projection = d3
    .geoNaturalEarth1()
    .scale(width / 1.3 / Math.PI)
    .translate([width / 2, height / 2]);

// Get the 'context'
const ctxMap = map.getContext("2d");
const ctxPoints = points.getContext("2d")

// geographic path generator for given projection and canvas context
const pathGenerator = d3.geoPath(projection, ctxMap);
const pathGeneratorPoints = d3.geoPath(projection, ctxPoints)

// Draw a background
// ctx.fillStyle = '#ddd';
// ctx.fillRect(0, 0, width, height);
async function getAndDrawData() {
    const data = await fetch("/wildfires")
    const response = await data.json()

    // initialize the path
    ctxPoints.beginPath();
    // Got the positions of the path
    const points = {
        type: "FeatureCollection",
        features: response.coords
    }

    pathGeneratorPoints(points);
    // Fill the paths
    // Add stroke
    ctxPoints.strokeStyle = "red";
    ctxPoints.stroke();
    console.log("Finished drawing")
}

getAndDrawData()
// Load external data and boot
d3.json(
    "https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson"
).then(function (data) {
    // initialize the path
    ctxMap.beginPath();
    // Got the positions of the path
    pathGenerator(data);
    // Fill the paths
    ctxMap.fillStyle = "white";
    ctxMap.fill();
    // Add stroke
    ctxMap.strokeStyle = "black";
    ctxMap.stroke();
});
