//vase course - pom
var height = 500;
function getData(data, key) {
    if (key==1)
        var ls = [["Courses", "Spent Hours"]];
    else
        var ls = [['Task', 'Hours per Day']]
    for (var member of data) {
        ls.push([member[0], member[key]]);
    }
    return ls;
}
function barChart(tag,title,info){
    google.charts.load('current', { 'packages': ['bar'] });
    google.charts.setOnLoadCallback(drawStuff);
    var ls = getData(info,1);
    function drawStuff() {
        var data = new google.visualization.arrayToDataTable(ls);
        var options = {
          height: window.height,
          chartArea: { width: "80%", height: "80%" },
          legend: { position: "none", alignment: "center" },
        //   chart: {
        //     title: title,
        //     subtitle: "Spent time per course",
        //   },
          bars: "horizontal",
          axes: {
            x: {
              0: { side: "down", label: "Spent Hours" },
            },
          },
          bar: { groupWidth: "80%" },
        };
        var chart = new google.charts.Bar(document.getElementById(tag));
        chart.draw(data, options);
    };
    };
//vase course - coin
function pieChart(tag,title,info){
    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart);
    var ls = getData(info,2);
    function drawChart() {
    var data = google.visualization.arrayToDataTable(ls);
    var options = {
      title: "Earned Coins Per Course",
      // 'title': title,
      titlePosition: "right",
      height: window.height,
      chartArea: { width: "80%", height: "80%" },
      legend: { position: "none", alignment: "center" },
    };
    var chart = new google.visualization.PieChart(document.getElementById(tag));
    chart.draw(data, options);
    };
};
// vase moghayese
function multiBarChart(tag) {
    google.charts.load('current', { 'packages': ['bar'] });
    google.charts.setOnLoadCallback(drawStuff);
    function drawStuff() {
        var data = new google.visualization.arrayToDataTable([
            ['Galaxy', 'Distance', 'Brightness'],
            ['Canis Major Dwarf', 8000, 23.3],
            ['Sagittarius Dwarf', 24000, 4.5],
            ['Ursa Major II Dwarf', 30000, 14.3],
            ['Lg. Magellanic Cloud', 50000, 0.9],
            ['Bootes I', 60000, 13.1]
        ]);
        var options = {
            width: 1800,
            chart: {
                title: 'Nearby galaxies',
                subtitle: 'distance on the left, brightness on the right'
            },
            bars: 'horizontal', // Required for Material Bar Charts.
            series: {
                0: { axis: 'distance' }, // Bind series 0 to an axis named 'distance'.
                1: { axis: 'brightness' } // Bind series 1 to an axis named 'brightness'.
            },
            axes: {
                x: {
                    distance: { label: 'parsecs' }, // Bottom x-axis.
                    brightness: { side: 'top', label: 'apparent magnitude' } // Top x-axis.
                }
            }
        };
        var chart = new google.charts.Bar(document.getElementById(tag));
        chart.draw(data, options);
    };
};