const configureFilter = document.querySelector('#configure-filter');
configureFilter.style.visibility = "collapse"
let toggle = configureFilter.style.visibility !== "collapse";

function toggleFilter(toggleElement) {
    toggleElement.style.borderBottomLeftRadius = toggle? "20px":"0";
    toggleElement.style.borderBottomRightRadius = toggle? "20px":"0";
    configureFilter.style.visibility = toggle ? 'collapse' : 'visible';
}

document.querySelector('#toggle-filter').addEventListener('click', function() {

    toggle = configureFilter.style.visibility !== "collapse";
    toggleFilter(this)

});


