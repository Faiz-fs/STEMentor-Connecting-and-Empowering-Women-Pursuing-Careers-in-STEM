let sliders = document.querySelectorAll('.slides .slide'),
    prevBtn = document.querySelector('.chevron-left'),
    nextBtn = document.querySelector('.chevron-right'),
    current = 0;

prevBtn.addEventListener('click', prevSlide);
nextBtn.addEventListener('click', nextSlide);

function showSlide(n) {
    //Remove active class from all slide
    sliders.forEach((slide) => {
        slide.classList.remove('active');
    });
    //Add class active to the current slide
    sliders[n].classList.add('active');
}

function nextSlide() {
    if (current < sliders.length - 1) {
        current++;
    } else {
        current = 0;
    }
    showSlide(current);
}

function prevSlide() {
    if (current <= 0) {
        current = sliders.length - 1;
    } else {
        current--;
    }
    showSlide(current);
}

setInterval(() => {
    nextSlide();
}, 3000);

nextSlide();
prevSlide();