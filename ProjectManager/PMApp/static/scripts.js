// Wait till DOMCOntentLoaded
window.addEventListener("DOMContentLoaded", (event) => {

    // Script to automatically redirect when selected new project using projct selector
    document.querySelectorAll("[name=project_selector]")[0].addEventListener('change',
    function () {
        window.location = "/switch_project/" + this.value;
    });
});


// Hides the div of either tasks or expenses lists
// and hides the button to create
function showNewForm(showType) {

    // Get the inverse of type and store it to hideType
    if (showType === "tasks") {
        var hideType = "expenses"
    } else {
        var hideType = "tasks"
    }

    // Get elements
    var divToHide = document.getElementById(hideType + "List");
    var divToShow = document.getElementById(showType + "Form");
    var btnToHide = document.getElementById(showType + "CreateBtn")

    // Hide and show elements
    // TODO: Edit based on the display set by bootstrap
    divToHide.style.display = "none";  
    divToShow.style.display = "block";
    btnToHide.style.display = "none";  
};


// Hides the div of the form to create either tasks or expenses
// and show the button to create
function closeNewForm(hideType) {

    // Get the inverse of type and store it to hideType
    if (hideType === "tasks") {
        var showType = "expenses"
    } else {
        var showType = "tasks"
    }
 
    // Get elements
    var divToHide = document.getElementById(hideType + "Form");
    var divToShow = document.getElementById(showType + "List");
    var btnToShow = document.getElementById(hideType + "CreateBtn");

    // Hide and show elements
    // TODO: Edit based on the display set by bootstrap
    divToHide.style.display = "none";  
    divToShow.style.display = "block";
    btnToShow.style.display = "inline-block";  
};