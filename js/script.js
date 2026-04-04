// Devran Wada - Main JavaScript

// Mobile Menu Toggle
const menuToggle = document.getElementById('menuToggle');
const navMenu = document.getElementById('navMenu');
const header = document.getElementById('header');

if (menuToggle) {
    menuToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        menuToggle.classList.toggle('active');
    });

    // Close menu when clicking on a link
    const navLinks = navMenu.querySelectorAll('a');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
            menuToggle.classList.remove('active');
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!menuToggle.contains(e.target) && !navMenu.contains(e.target)) {
            navMenu.classList.remove('active');
            menuToggle.classList.remove('active');
        }
    });
}

// Hero Slider
const heroSlides = document.querySelectorAll('.hero-slide');
const prevSlideBtn = document.getElementById('prevSlide');
const nextSlideBtn = document.getElementById('nextSlide');

if (heroSlides.length > 0) {
    let currentSlide = 0;
    const totalSlides = heroSlides.length;

    function showSlide(index) {
        heroSlides.forEach(slide => slide.classList.remove('active'));
        heroSlides[index].classList.add('active');
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % totalSlides;
        showSlide(currentSlide);
    }

    function prevSlide() {
        currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
        showSlide(currentSlide);
    }

    // Auto slide every 5 seconds
    let autoSlide = setInterval(nextSlide, 5000);

    if (nextSlideBtn) {
        nextSlideBtn.addEventListener('click', () => {
            clearInterval(autoSlide);
            nextSlide();
            autoSlide = setInterval(nextSlide, 5000);
        });
    }

    if (prevSlideBtn) {
        prevSlideBtn.addEventListener('click', () => {
            clearInterval(autoSlide);
            prevSlide();
            autoSlide = setInterval(nextSlide, 5000);
        });
    }
}

// Gallery Filter
const filterButtons = document.querySelectorAll('.filter-btn');
const galleryItems = document.querySelectorAll('.gallery-item');

if (filterButtons.length > 0) {
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove active class from all buttons
            filterButtons.forEach(btn => btn.classList.remove('active'));
            // Add active class to clicked button
            button.classList.add('active');

            const filterValue = button.getAttribute('data-filter');

            galleryItems.forEach(item => {
                if (filterValue === 'all') {
                    item.style.display = 'block';
                    item.classList.add('fade-in');
                } else {
                    if (item.getAttribute('data-category') === filterValue) {
                        item.style.display = 'block';
                        item.classList.add('fade-in');
                    } else {
                        item.style.display = 'none';
                    }
                }
            });
        });
    });
}

// Contact Form Handling (Formspree)
const contactForm = document.getElementById('contactForm');
const formStatus = document.getElementById('form-status');

if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        const submitBtn = contactForm.querySelector('button[type="submit"]');
        const originalBtnText = submitBtn.textContent;
        
        // Show loading state
        submitBtn.disabled = true;
        submitBtn.textContent = 'Sending...';
        
        // Form will submit to Formspree
        // After submission, Formspree will redirect or show confirmation
    });
}

// Smooth Scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Header scroll effect
let lastScroll = 0;
const scrollThreshold = 100;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    // Add scrolled class for styling
    if (currentScroll > scrollThreshold) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
    
    lastScroll = currentScroll;
});

// Scroll Reveal Animation
const revealElements = document.querySelectorAll('.feature-card, .project-card, .gallery-item, .facility-card, .value-card, .testimonial-card');

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
            setTimeout(() => {
                entry.target.classList.add('fade-in');
            }, index * 100);
            revealObserver.unobserve(entry.target);
        }
    });
}, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
});

revealElements.forEach(el => {
    revealObserver.observe(el);
});

// Tap to Play for Testimonial Video 4
const tapToPlayVideos = document.querySelectorAll('.tap-to-play');

tapToPlayVideos.forEach(video => {
    video.addEventListener('click', function() {
        if (this.paused) {
            this.play();
        } else {
            this.pause();
        }
    });
    
    // Add visual indicator
    video.style.cursor = 'pointer';
});
