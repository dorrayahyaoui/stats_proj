var employeeLabel = [], employeeSalaryData = [], employeeAgeData = []

async function dummyChart() {
  await getDummyData()

const ctx = document.getElementById('myChart').getContext('2d');

const chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'bar',

    // The data for our dataset
    data: {
        labels: employeeLabel,
        datasets: [{
            label: 'Employee Salary',
            backgroundColor: 'blue',
            borderColor: 'rgb(255, 99, 132)',
            data: employeeSalaryData
        },
        {
          label: 'Employee Age',
          backgroundColor: 'pink',
          borderColor: 'rgb(255, 99, 132)',
          data: employeeAgeData
      }
      ]
    },

    // Configuration options go here
    options: {
      tooltips: {
        mode: 'index'
      }
    }
})}

dummyChart()


//Fetch Data from API

async function getDummyData() {
  var formdata = new FormData();
  formdata.append("ID", "11");
  const apiUrl = "http://dummy.restapiexample.com/api/v1/employees"
  const apiUrl2 = "http://127.0.0.1:8000/api/cachier/monthly"
  const response2 = await fetch(apiUrl2,{method: 'POST', body: formdata , redirect: 'follow', headers:{ "X-CSRFToken": '{{csrf_token}}' },})
  console.log(response2)
  const response = await fetch(apiUrl)
  const barChatData = await response.json()
  const barChatData2 = await response2.json()
  console.log(barChatData2)
  const salary = barChatData.data.map((x) => x.employee_salary)
  console.log(salary)
  const age = barChatData.data.map((x) => x.employee_age)
  const name = barChatData.data.map((x) => x.employee_name)

 employeeSalaryData = salary
 employeeAgeData = age
 employeeLabel = name
}