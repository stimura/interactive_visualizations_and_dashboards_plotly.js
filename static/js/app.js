// Step 1: Set up our chart
//= ================================
// var svgWidth = 960;
// var svgHeight = 500;

// var margin = {
//   top: 20,
//   right: 40,
//   bottom: 60,
//   left: 50
// };

// var width = svgWidth - margin.left - margin.right;
// var height = svgHeight - margin.top - margin.bottom;

var all_names = new Array();

function names() {
  Plotly.d3.json('/names', function(error, response) {
    all_names = response;
    all_names.forEach(name => {
      var option = Plotly.d3.select('#selDataset').append('option').attr('value', name).text(name);
    });
  });
};

names();

function pie_chart() {
  Plotly.d3.json('/pie', function(error, data) {
              if (error) return console.warn(error);

              var layout = {
                  title: "UTO"}
              var PIE = document.getElementById('pie');
              Plotly.plot(PIE, data, layout);
          })
};

pie_chart();