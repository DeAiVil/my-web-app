document.addEventListener("scroll", function () {
    let parallax = document.querySelector(".parallax");
    let scrollPosition = window.scrollY;
    parallax.style.transform = `translateY(${scrollPosition * 0.5}px)`; // Двигаем фон медленнее
});
