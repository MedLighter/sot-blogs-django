document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("button1");
    const rect = document.getElementById("rect1");

    button.addEventListener("click", () => {
        toggleTwoClasses(rect, "is-visible", "is-hidden", 500);
        button.style.display = "none";
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("button2");
    const rect = document.getElementById("rect2");

    button.addEventListener("click", () => {
        toggleTwoClasses(rect, "is-visible", "is-hidden", 500);
        button.style.display = "none";
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("button3");
    const rect = document.getElementById("rect3");

    button.addEventListener("click", () => {
        toggleTwoClasses(rect, "is-visible", "is-hidden", 500);
        button.style.display = "none";
    });
});



document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("button4");
    const rect = document.getElementById("rect4");

    button.addEventListener("click", () => {
        toggleTwoClasses(rect, "is-visible", "is-hidden", 500);
        button.style.display = "none";
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("button5");
    const rect = document.getElementById("rect5");

    button.addEventListener("click", () => {
        toggleTwoClasses(rect, "is-visible", "is-hidden", 500);
        button.style.display = "none";
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("button6");
    const rect = document.getElementById("rect6");

    button.addEventListener("click", () => {
        toggleTwoClasses(rect, "is-visible", "is-hidden", 500);
        button.style.display = "none";
    });
});


function toggleTwoClasses(element, first, second, timeOfAnimation) {
    if (!element.classList.contains(first)) {
        element.classList.add(first);
        element.classList.remove(second);
    } else {
        element.classList.add(second);
        window.setTimeout(function () {
            element.classList.remove(first);
        }, timeOfAnimation);
    }
}