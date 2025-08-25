// Update copyright year
document.getElementById('year').textContent = new Date().getFullYear();

// Mobile menu toggle
document.getElementById('menu-toggle').addEventListener('click', function() {
    document.getElementById('mobile-menu').classList.toggle('hidden');
});

// Smooth scrolling for all internal links
// Smooth scrolling for all links with hashes (even with absolute URLs)
document.querySelectorAll('a[href*="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const url = new URL(this.href);
        const hash = url.hash;
        const target = document.querySelector(hash);

        // Only handle in-page scrolling for links pointing to the current page
        if (target && url.pathname === window.location.pathname) {
            e.preventDefault();

            // Scroll smoothly
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });

            // Close mobile menu if open
            document.getElementById('mobile-menu').classList.add('hidden');

            // Update active nav link
            document.querySelectorAll('.nav-link').forEach(link => link.classList.remove('active'));
            this.classList.add('active');

            // Update URL hash without jumping
            history.pushState(null, null, hash);
        }
    });
});

// Highlight active nav link on scroll
window.addEventListener('scroll', function() {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-link');
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// Contact form submission with POST to Django
const contactForm = document.getElementById('contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(this);

        fetch("", {  // POST to the same URL
            method: "POST",
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: formData
        })
        .then(response => {
            if (!response.ok) throw new Error("Network response was not ok");
            return response.text();
        })
        .then(data => {
            // Show thank you alert
            const name = document.getElementById('name').value;
            alert(`Thank you, ${name}! Your message has been sent.`);
            contactForm.reset();
        })
        .catch(error => {
            alert("Failed to send message. Please try again.");
            console.error("Error:", error);
        });
    });
}

// Intersection Observer for fade-in animations
const observerOptions = { threshold: 0.1 };
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-fade-in');
        }
    });
}, observerOptions);

document.querySelectorAll('section').forEach(section => observer.observe(section));
