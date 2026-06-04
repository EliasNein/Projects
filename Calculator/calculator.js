let calculation = localStorage.getItem('calculation') || '';
function calculateCalculation(value) {
  calculation += value;
  saveCalculation();
  displayCalculation();
}

function displayCalculation() {
  document.querySelector('.showCalculation').value = calculation;
}

function saveCalculation() {
  displayCalculation();
  localStorage.setItem('calculation', calculation);
}