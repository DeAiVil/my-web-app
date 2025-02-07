document.addEventListener("DOMContentLoaded", function () {
    const sections = document.querySelectorAll("section");
    
    function reveal() {
        sections.forEach((section) => {
            const windowHeight = window.innerHeight;
            const sectionTop = section.getBoundingClientRect().top;
            if (sectionTop < windowHeight - 100) {
                section.style.opacity = "1";
                section.style.transform = "translateY(0)";
            }
        });
    }
    
    sections.forEach((section) => {
        section.style.opacity = "0";
        section.style.transform = "translateY(50px)";
        section.style.transition = "opacity 0.6s ease-out, transform 0.6s ease-out";
    });
    
    window.addEventListener("scroll", reveal);
    reveal();
});
