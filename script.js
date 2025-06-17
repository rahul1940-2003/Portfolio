/* menu icon navbar */
let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menuIcon.onclick = () => {
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
};



/* Scroll sections active link */

let sections = document.querySelectorAll('section'); // Fix 1: Select all sections
let navLinks = document.querySelectorAll('header nav a');

window.onscroll = () => {
    let top = window.scrollY;

    sections.forEach(sec => {
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let di = sec.getAttribute('id'); // Fix 2: Use `di` correctly

        if (top >= offset && top < offset + height) {
            navLinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('header nav a[href*="' + di + '"]').classList.add('active'); // Fix 2: Correct variable name
            });
        }
    });

    /* Sticky Navbar */
    let header = document.querySelector('.header');
    header.classList.toggle('sticky', window.scrollY > 100);

    /* ==== remove menu icon navbar when click navbar Link (scroll) */
        menuIcon.classList.remove('bx-x');
        navbar.classList.remove('active');
    
    
    

};

/* Swiper */
var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 50,
    loop: true,
    grabCursor: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },

});


/*========== Dark Light mode ========*/ 

let darkModeIcon = document.querySelector('#darkMode-icon');

darkModeIcon.onclick = () => {
    darkModeIcon.classList.toggle('bx-sun');
    document.body.classList.toggle('dark-mode');
};

/*========== scroll reveal ========*/ 

ScrollReveal({
    reset: true,
    distance: '80px',
    duration: 2000,
    delay: 200
   
});

ScrollReveal().reveal('.home-content, .heading', { origin: 'top' });
ScrollReveal().reveal('.home-img img, .services-container, .portfolio-box, .testimonial-wrapper, .contant form', { origin: 'bottom' });
ScrollReveal().reveal('.home-content h1, .about-img img', { origin: 'left'});
ScrollReveal().reveal('.home-content h3, .home-content p, .about-content', { origin: 'right'});



