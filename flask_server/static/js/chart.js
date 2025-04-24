// flask_server/static/js/charts.js
window.addEventListener('DOMContentLoaded', (event) => {
  fetch('/api/blood_pressure')
    .then(response => response.json())
    .then(data => {
      // Giả sử dữ liệu có trường timestamp và systolic để vẽ biểu đồ theo thời gian
      const labels = data.map(item => new Date(item.timestamp).toLocaleTimeString());
      const systolicData = data.map(item => item.systolic);
      
      const ctx = document.getElementById('bpChart').getContext('2d');
      new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
            label: 'Huyết áp tâm thu',
            data: systolicData,
            borderColor: 'rgba(255, 99, 132, 1)',
            fill: false
          }]
        },
        options: {
          scales: {
            x: {
              title: {
                display: true,
                text: 'Thời gian'
              }
            },
            y: {
              title: {
                display: true,
                text: 'Giá trị'
              }
            }
          }
        }
      });
    })
    .catch(error => console.error("Lỗi khi lấy dữ liệu:", error));
});
