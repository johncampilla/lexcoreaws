const totalmattersindustry = document.getElementById('total-matters-industry');
const totalmattersapptype = document.getElementById('total-matters-apptype');
const totalmatterslawyers = document.getElementById('total-matters-lawyers');
const totalmattersfolders = document.getElementById('total-matters-folders');
const totalmatterscasetype = document.getElementById('total-matters-casetype');
const totalmattersnature = document.getElementById('total-matters-nature');

const datatable = document.getElementById('datatable');

fetch('/totalindustry/')
.then(res => res.json())
.then(data => {
    new Chart(totalmattersindustry, {
        type: 'line',
        data: {
        labels: data.labels,
        datasets: [{
            label: '# of matters',
            data: data.data,
            backgroundColor: [
            'rgba(255, 99, 132, 1)',
            // 'rgba(54, 162, 235, 1)',
            // 'rgba(255, 206, 86, 1)',
            // 'rgba(75, 192, 192, 1)',
            // 'rgba(153, 102, 255, 1)',
            // 'rgba(255, 159, 64, 1)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                // 'rgba(54, 162, 235, 1)',
                // 'rgba(255, 206, 86, 1)',
                // 'rgba(75, 192, 192, 1)',
                // 'rgba(153, 102, 255, 1)',
                // 'rgba(255, 159, 64, 1)'
            ],
                borderWidth: 2
            }]
        },
        options: {
        scales: {
                y: {
                beginAtZero: true
                }
            }
        }
    })
})

fetch('/totalapptype/')
.then(res => res.json())
.then(data => {const mattersapptype = new Chart(totalmattersapptype, {
    type: 'line',
    data: {
        labels: data.labels,
        datasets: [{
        label: '# of matters',
        data: data.data,
        backgroundColor: [
            'rgba(255, 99, 132, 1)',
            // 'rgba(54, 162, 235, 1)',
            // 'rgba(255, 206, 86, 1)',
            // 'rgba(75, 192, 192, 1)',
            // 'rgba(153, 102, 255, 1)',
            // 'rgba(255, 159, 64, 1)'
        ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                // 'rgba(54, 162, 235, 1)',
                // 'rgba(255, 206, 86, 1)',
                // 'rgba(75, 192, 192, 1)',
                // 'rgba(153, 102, 255, 1)',
                // 'rgba(255, 159, 64, 1)'
            ],
                borderWidth: 2
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
})
})


fetch('/totallawyers/')
.then(res => res.json())
.then(data => {const matterslawyers = new Chart(totalmatterslawyers, {
    type: 'bar',
    data: {
        labels: data.labels,
        datasets: [{
        label: '',
        data: data.data,
        backgroundColor: [
            'rgba(255, 99, 132, 1)',
            // 'rgba(54, 162, 235, 1)',
            // 'rgba(255, 206, 86, 1)',
            // 'rgba(75, 192, 192, 1)',
            // 'rgba(153, 102, 255, 1)',
            // 'rgba(255, 159, 64, 1)'
        ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                // 'rgba(54, 162, 235, 1)',
                // 'rgba(255, 206, 86, 1)',
                // 'rgba(75, 192, 192, 1)',
                // 'rgba(153, 102, 255, 1)',
                // 'rgba(255, 159, 64, 1)'
            ],
                borderWidth: 2
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
})
})

fetch('/totalfolders/')
.then(res => res.json())
.then(data => {const mattersfolders = new Chart(totalmattersfolders, {
    type: 'bar',
    data: {
        labels: data.labels,
        datasets: [{
        label: '',
        data: data.data,
        backgroundColor: [
            'rgba(255, 99, 132, 1)',
            // 'rgba(54, 162, 235, 1)',
            // 'rgba(255, 206, 86, 1)',
            // 'rgba(75, 192, 192, 1)',
            // 'rgba(153, 102, 255, 1)',
            // 'rgba(255, 159, 64, 1)'
        ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                // 'rgba(54, 162, 235, 1)',
                // 'rgba(255, 206, 86, 1)',
                // 'rgba(75, 192, 192, 1)',
                // 'rgba(153, 102, 255, 1)',
                // 'rgba(255, 159, 64, 1)'
            ],
                borderWidth: 2
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
})
})


fetch('/totalcasetype/')
.then(res => res.json())
.then(data => {const matterscasetype = new Chart(totalmatterscasetype, {
    type: 'bar',
    data: {
        labels: data.labels,
        datasets: [{
        label: '',
        data: data.data,
        backgroundColor: [
            'rgba(255, 99, 132, 1)',
            // 'rgba(54, 162, 235, 1)',
            // 'rgba(255, 206, 86, 1)',
            // 'rgba(75, 192, 192, 1)',
            // 'rgba(153, 102, 255, 1)',
            // 'rgba(255, 159, 64, 1)'
        ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                // 'rgba(54, 162, 235, 1)',
                // 'rgba(255, 206, 86, 1)',
                // 'rgba(75, 192, 192, 1)',
                // 'rgba(153, 102, 255, 1)',
                // 'rgba(255, 159, 64, 1)'
            ],
                borderWidth: 2
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
})
})

fetch('/totalnature/')
.then(res => res.json())
.then(data => {const matterscasetype = new Chart(totalmattersnature, {
    type: 'bar',
    data: {
        labels: data.labels,
        datasets: [{
        label: '',
        data: data.data,
        backgroundColor: [
            'rgba(255, 99, 132, 1)',
            // 'rgba(54, 162, 235, 1)',
            // 'rgba(255, 206, 86, 1)',
            // 'rgba(75, 192, 192, 1)',
            // 'rgba(153, 102, 255, 1)',
            // 'rgba(255, 159, 64, 1)'
        ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                // 'rgba(54, 162, 235, 1)',
                // 'rgba(255, 206, 86, 1)',
                // 'rgba(75, 192, 192, 1)',
                // 'rgba(153, 102, 255, 1)',
                // 'rgba(255, 159, 64, 1)'
            ],
                borderWidth: 2
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
})
})
