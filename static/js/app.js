
// Timer for notification messages (login-logout)

var message_timeout = document.getElementById("message-timer");

setTimeout(function()

{

    message_timeout.style.display = "none";


}, 2500);


// Function for adding numbers 

// static/js/app.js
function calculateTotal() {
    // Get all the rows in the table body
    const rows = document.querySelectorAll("#expenseTable tbody tr");
    let totalCost = 0;

    // Loop through each row and add the cost to the total
    rows.forEach(row => {
        const cost = parseFloat(row.querySelector(".cost").textContent) || 0;
        totalCost += cost;
    });

    // Update the total cost displayed in the table footer
    document.getElementById("totalCost").textContent = totalCost.toFixed(2);
}

// Call the calculateTotal function once the page has loaded
document.addEventListener('DOMContentLoaded', function() {
    calculateTotal();
});