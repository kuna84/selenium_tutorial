const links = document.querySelectorAll(".topnav a");

links.forEach(link => {
    if (link.href === window.location.href) {
        link.classList.add("active");
    }

    link.addEventListener("click", () => {
        links.forEach(link => link.classList.remove("active"));
        link.classList.add("active");
    });
});