//vase course - pom
var height = 500;
function barChart(tag,title){
    google.charts.load('current', { 'packages': ['bar'] });
    google.charts.setOnLoadCallback(drawStuff);
    function drawStuff() {
        var data = new google.visualization.arrayToDataTable([
            ['Courses', 'Pomodoros'],
            ["Course 1", 44],
            ["Course 2", 44],
            ["Course 3", 44],
            ["Course 4", 44],
        ]);
        var options = {
            title: title,
            width: 900,
            height:window.height,
            legend: { position: 'none' },
            chart: {
                title: title,
                subtitle: 'Completed pomodoros per course'
            },
            bars: 'horizontal', // Required for Material Bar Charts.
            axes: {
                x: {
                    0: { side: 'top', label: 'Completed pomodoros' } // Top x-axis.
                }
            },
            bar: { groupWidth: "90%" }
        };
        var chart = new google.charts.Bar(document.getElementById(tag));
        chart.draw(data, options);
    };
    };
//vase course - coin
function pieChart(tag,title){
    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Task', 'Hours per Day'],
        ['Course1',     11],
        ['Course2',      2],
        ['Course3',  2],
        ['Course4', 2],
    ]);
    var options = {
        title: title,
        height: window.height,
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