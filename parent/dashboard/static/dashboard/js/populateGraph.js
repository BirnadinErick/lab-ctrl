(function($) {
    /* "use strict" */

    var dzChartlist = function() {

        var healthyChildrenPlot = function() {
            $("span.donut-1").peity("donut", {
                width: "86",
                height: "86"
            });
        }
        var rogueChildrenPlot = function() {
            $("span.donut-2").peity("donut", {
                width: "232",
                height: "232"
            });
        }

        var STasksReport = function() {
            var options1 = {
                    series: [{ data: [25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54] }],
                    fill: { colors: ["#3C21F7"] },
                    chart: { type: "line", width: 70, height: 40, sparkline: { enabled: !0 } },
                    plotOptions: { bar: { columnWidth: "50%" } },
                    labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                    xaxis: { crosshairs: { width: 1 } },
                    tooltip: {
                        fixed: { enabled: !1 },
                        x: { show: !1 },
                        y: {
                            title: {
                                formatter: function(e) {
                                    return "";
                                },
                            },
                        },
                        marker: { show: !1 },
                    },
                },
                chart1 = new ApexCharts(document.querySelector("#total-revenue-chart"), options1);
            chart1.render();
        }

        var STasksCompare = function() {
            var options1 = {
                    series: [{ data: [55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54] }],
                    fill: { colors: ["#3C21F7"] },
                    chart: { type: "line", width: 70, height: 40, sparkline: { enabled: !0 } },
                    plotOptions: { bar: { columnWidth: "50%" } },
                    labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                    xaxis: { crosshairs: { width: 1 } },
                    tooltip: {
                        fixed: { enabled: !1 },
                        x: { show: !1 },
                        y: {
                            title: {
                                formatter: function(e) {
                                    return "";
                                },
                            },
                        },
                        marker: { show: !1 },
                    },
                },
                chart1 = new ApexCharts(document.querySelector("#total-revenue-chart-1"), options1);
            chart1.render();
        }

        $('.canvas-container').each(function(index, el) {

            var width = $(this).width();
            var height = width + width * .25;
            var data = [];
            var colors = [];
            var labels = [];
            $(el).find('.chart-data > *').each(function() {
                data.push(parseInt($(this).attr('data-percent')));
                colors.push($(this).attr('data-color'));
                labels.push($(this).attr('data-label'));
            })

            $('#chartjs-4').attr('width', width).attr('height', height);
            new Chart(document.getElementById("chartjs-4"), {
                "type": "doughnut",
                responsive: true,
                options: {
                    legend: {
                        display: false,
                    }

                },
                maintainAspectRatio: false,
                "data": {
                    "labels": labels,
                    "datasets": [{
                        "data": data,
                        "backgroundColor": colors
                    }]
                }
            });
        })

        /* Function ============ */
        return {
            init: function() {},


            load: function() {
                // Healthy Children Plot
                healthyChildrenPlot();
                // Rogue Children Plot
                rogueChildrenPlot();
                // S Tasks Report
                STasksReport();
                //  S Tasks Compare
                STasksCompare();
            },

            resize: function() {

            }
        }

    }();

    jQuery(document).ready(function() {});

    jQuery(window).on('load', function() {
        setTimeout(function() {
            dzChartlist.load();
        }, 1000);

    });

    jQuery(window).on('resize', function() {


    });

})(jQuery);

let meanload_options = {
    series: [{
        name: "CPU %",
        data: []
    }, {
        name: "Memory %",
        data: []
    }],
    colors: ['#b33c86ff', '#190e4fff'],
    chart: {
        height: 300,
        type: 'line',
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        curve: 'smooth'
    },
    xaxis: {
        categories: [],
    },


}

let customer_chart = new ApexCharts(document.querySelector("#mean-chart"), meanload_options)
customer_chart.render()

function populateMeanLoadGraph() {
    fetch(`http://${mother}/api/meandata`)
        .then(res => res.json())
        .then((new_data) => {
            customer_chart.updateOptions({
                series: [{
                    name: new_data.cpu.name,
                    data: new_data.cpu.data
                }, {
                    name: new_data.mem.name,
                    data: new_data.mem.data
                }],
                xaxis: {
                    categories: new_data.cat.categories,
                }
            })
        });
}
populateMeanLoadGraph();
// TODO: Change the interval according to the user preference
setInterval(populateMeanLoadGraph, 1000 * 60);