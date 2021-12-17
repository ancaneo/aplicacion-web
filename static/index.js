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
const exampleData = {
  type: "FeatureCollection",
  features: [
    {
      type: "Feature",
      properties: {},
      geometry: {
        type: "Point",
        coordinates: [-63.896484375, -12.768946439455943],
      },
    },
    {
      type: "Feature",
      properties: {},
      geometry: {
        type: "Point",
        coordinates: [-74.970703125, -13.282718960896405],
      },
    },
    {
      type: "Feature",
      properties: {},
      geometry: {
        type: "Point",
        coordinates: [-68.9501953125, -23.120153621695614],
      },
    },
    {
      type: "Feature",
      properties: {},
      geometry: {
        type: "Point",
        coordinates: [-69.873046875, -25.244695951306028],
      },
    },
    {
      type: "Feature",
      properties: {},
      geometry: {
        type: "Point",
        coordinates: [-70.83984375, -15.368949896534705],
      },
    },
    {
      type: "Feature",
      properties: {},
      geometry: {
        type: "Point",
        coordinates: [-75.89355468749999, -10.574222078332806],
      },
    },
    {
      type: "Feature",
      properties: {},
      geometry: {
        type: "Point",
        coordinates: [-72.99316406249999, -13.88074584202559],
      },
    },
  ],
};

// initialize the path
ctxPoints.beginPath();
// Got the positions of the path
pathGeneratorPoints(exampleData);
// Fill the paths
ctxPoints.fillStyle = "red";
ctxPoints.fill();
// Add stroke
ctxPoints.strokeStyle = "red";
ctxPoints.stroke();

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
