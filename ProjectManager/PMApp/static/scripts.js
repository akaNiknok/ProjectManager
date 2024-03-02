// Wait till DOMCOntentLoaded
window.addEventListener("DOMContentLoaded", (event) => {

    // Script to automatically redirect when selected new project using projct selector
    document.querySelectorAll("[name=project_selector]")[0].addEventListener('change',
    function () {
        window.location = "/switch_project/" + this.value;
    });
});


// Hides the div of either tasks or expenses
// and shows the appropriate form
function showNewForm(type) {

    // Get the inverse of type and store it to hideType
    if (type === "tasks") {
        var hideType = "expenses"
    } else {
        var hideType = "tasks"
    }

    // Hide the div
    var divToHide = document.getElementById(hideType);
    if (divToHide.style.display === "none") {
        // TODO: Might need to change based on display set by Bootstrap
        divToHide.style.display = "block";  
    } else {
        divToHide.style.display = "none";
    };

    // Show the form
}