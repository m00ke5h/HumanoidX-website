let slideIndex = 1;
carousel(slideIndex);
// Next/previous controls
function plusSlides(n) {
    carousel((slideIndex += n));
}

// Thumbnail image controls
function currentSlide(n) {
    carousel((slideIndex = n));
}

function carousel(n) {
    let slides = document.getElementsByClassName("slide-item");
    let dots = document.getElementsByClassName("dot");
    if (n > slides.length) {
        slideIndex = 1;
    }
    if (n < 1) {
        slideIndex = slides.length;
    }
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (let i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    slides[slideIndex - 1].className += " fade-in";
    dots[slideIndex - 1].className += " active";
}