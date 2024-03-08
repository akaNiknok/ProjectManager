// Wait till DOMCOntentLoaded
window.addEventListener("DOMContentLoaded", (event) => {

    // Script to automatically redirect when selected new project using projct selector
    document.querySelectorAll("[name=project_selector]")[0].addEventListener('change',
    function () {
        window.location = "/switch_project/" + this.value;
    });
});


// Toggle the div of the create form of the 'type',
// the div for the list of the 'oppositeType',
// and the button to create new 'type'
function toggleForm(type) {

    // Get the opposite type
    var oppositeType = (type === "tasks") ? "expenses" : "tasks";

    // Get the elements to toggle
    var divType = document.getElementById(type + "Form");
    var divOpposite = document.getElementById(oppositeType + "List");
    var btnType = document.getElementById(type + "CreateBtn");

    // Get the current display value of each element
    var divTypeCurrentStyle = window.getComputedStyle(divType).getPropertyValue("display");
    var divOppositeCurrentStyle = window.getComputedStyle(divOpposite).getPropertyValue("display");
    var btnTypeCurrentStyle = window.getComputedStyle(btnType).getPropertyValue("display");
    
    // Toggle the values
    divType.style.display = divTypeCurrentStyle === "none" || "" ? "block" : "none";
    divOpposite.style.display = divOppositeCurrentStyle === "none" ? "block" : "none";
    btnType.style.display = btnTypeCurrentStyle === "none" ? "inline-block" : "none";
}