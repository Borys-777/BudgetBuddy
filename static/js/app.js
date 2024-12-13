// Timer for notification messages (login-logout)

var message_timeout = document.getElementById("message-timer");

setTimeout(function ()

    {
        message_timeout.style.display = "none";

    }, 2500);


// Function for adding numbers (total cost)

function calculateTotal() {

    const rows = document.querySelectorAll("#expenseTable tbody tr");
    let totalCost = 0;

    rows.forEach(row => {
        const cost = parseFloat(row.querySelector(".cost").textContent) || 0;
        totalCost += cost;
    });

    document.getElementById("totalCost").textContent = totalCost.toFixed(2);
}

document.addEventListener('DOMContentLoaded', function () {
    calculateTotal();
});