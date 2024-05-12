// Function to update the session storage with the current body class
function updateBodyClassInSession() {
    const bodyClass = document.body.classList.value;
    sessionStorage.setItem('body_class', bodyClass);
}

// Function to retrieve the body class from session storage and apply it to the body
function applyBodyClassFromSession() {
    const bodyClass = sessionStorage.getItem('body_class');
    if (bodyClass) {
        document.body.className = bodyClass;
    }
}

// Call the function to apply body class from session storage when the DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    applyBodyClassFromSession();
});

// Call the function to update body class in session storage whenever the body class changes
document.addEventListener('DOMContentLoaded', function() {
    document.body.addEventListener('click', function() {
        updateBodyClassInSession();
    });
});