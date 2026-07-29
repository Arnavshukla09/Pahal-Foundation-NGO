// home elements
document.addEventListener("DOMContentLoaded",()=>{

// Counter Animation
const counters = document.querySelectorAll(".counter");
const speed = 200;

const animateCounter = (counter) => {
    const target = parseInt(counter.getAttribute("data-target"));

    if (isNaN(target)) return;   // Safety check

    let count = 0;
    const increment = target / speed;

    const updateCount = () => {
        count += increment;

        if (count < target) {
            counter.innerText = Math.ceil(count);
            requestAnimationFrame(updateCount);
        } else {
            counter.innerText = target + "+";
        }
    };

    updateCount();
};

counters.forEach(counter => {
    animateCounter(counter);
});

window.addEventListener('load', function() {
    const preloader = document.getElementById('preloader');
    const heroVideo = document.getElementById('heroVideo');

    // Check if the user has already seen the preloader in this session
    if (sessionStorage.getItem('preloaderPlayed')) {
        // Hide preloader immediately without animation
        preloader.style.display = 'none';
        document.body.style.overflow = 'auto';
        
        // Start video immediately
        if(heroVideo) heroVideo.play();
    } else {
        // First time visit: Play animation
        if(heroVideo) heroVideo.pause();

        setTimeout(() => {
            preloader.classList.add('preloader-hidden');
            
            if(heroVideo) {
                heroVideo.play().catch(error => console.log("Auto-play blocked"));
            }
            
            document.body.style.overflow = 'auto';
            
            // Mark the session so it doesn't play again
            sessionStorage.setItem('preloaderPlayed', 'true');
        }, 3000); 
    }
});

    // Scroll Reveal Animation
    const scrollReveal = () => {
      const elements = document.querySelectorAll(".scroll-reveal")
      elements.forEach((element) => {
        const elementTop = element.getBoundingClientRect().top
        const elementVisible = 150
  
        if (elementTop < window.innerHeight - elementVisible) {
          element.classList.add("active")
        }
      })
    }
  
    // Initialize counter animation when elements are in view
    const observeCounters = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateCounter(entry.target)
          observeCounters.unobserve(entry.target)
        }
      })
    })
  
    counters.forEach((counter) => observeCounters.observe(counter))
  
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
      anchor.addEventListener("click", function (e) {
        e.preventDefault()
        const target = document.querySelector(this.getAttribute("href"))
        if (target) {
          target.scrollIntoView({
            behavior: "smooth",
          })
        }
      })
    })
    // Back to top button functionality
      const backToTop = document.querySelector(".back-to-top");

    window.addEventListener("scroll", function () {
        if (window.scrollY > 300) {
            backToTop.classList.add("show");
        } else {
            backToTop.classList.remove("show");
        }
    });

    backToTop.addEventListener("click", function (e) {
        e.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });
    // Parallax effect for hero section
    const hero = document.querySelector(".hero")
    window.addEventListener("scroll", () => {
      const scrolled = window.pageYOffset
      hero.style.backgroundPositionY = scrolled * 0.5 + "px"
    })
  
    // Initialize scroll reveal animation
    window.addEventListener("scroll", scrollReveal)
    scrollReveal()
  
    // Navbar scroll effect
    const nav = document.querySelector("nav")
    let lastScroll = 0
  
    window.addEventListener("scroll", () => {
      const currentScroll = window.pageYOffset
  
      if (currentScroll <= 0) {
        nav.classList.remove("scroll-up")
        return
      }
  
      if (currentScroll > lastScroll && !nav.classList.contains("scroll-down")) {
        nav.classList.remove("scroll-up")
        nav.classList.add("scroll-down")
      } else if (currentScroll < lastScroll && nav.classList.contains("scroll-down")) {
        nav.classList.remove("scroll-down")
        nav.classList.add("scroll-up")
      }
      lastScroll = currentScroll
    })
  
    // Value cards hover effect
    const valueCards = document.querySelectorAll(".value-card")
    valueCards.forEach((card) => {
      card.addEventListener("mouseenter", () => {
        card.style.transform = "translateY(-10px)"
      })
      card.addEventListener("mouseleave", () => {
        card.style.transform = "translateY(0)"
      })
    })
  
    // Team member image hover effect
    const teamMembers = document.querySelectorAll(".team-member")
    teamMembers.forEach((member) => {
      const image = member.querySelector("img")
      member.addEventListener("mouseenter", () => {
        image.style.transform = "scale(1.1)"
      })
      member.addEventListener("mouseleave", () => {
        image.style.transform = "scale(1)"
      })
    })

    // Animation for impact items
    const impactItems = document.querySelectorAll(".impact-item")

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.style.opacity = 1
            entry.target.style.transform = "translateY(0)"
          }
        })
      },
      { threshold: 0.5 },
    )

    impactItems.forEach((item) => {
      item.style.opacity = 0
      item.style.transform = "translateY(20px)"
      item.style.transition = "all 0.5s ease-out"
      observer.observe(item)
    })
  })

pizza = document.querySelector('.pizza')
navbar = document.querySelector('.nav-bar')
navlinks = document.querySelector('.nav-links')

pizza.addEventListener('click',()=>{
    navbar.classList.toggle('h-nav-resp')
    navlinks.classList.toggle('nav-links-res')
    pizza.classList.toggle('pizza')
})
// Donation Form Submission
document.addEventListener("DOMContentLoaded", function () {
    const donationForm = document.getElementById("donationForm");

    if (donationForm) {
        donationForm.addEventListener("submit", async function (e) {
            e.preventDefault();

            const formData = new FormData(donationForm);

            try {
                const response = await fetch(donationForm.action, {
                    method: "POST",
                    body: formData
                });

                const result = await response.json();

                if (result.success) {
                    alert("Donation request submitted successfully!");
                    donationForm.reset();
                } else {
                    alert("Something went wrong. Please try again.");
                }

            } catch (error) {
                alert("Error submitting form.");
            }
        });
    }
});
function openModal(id) {
    document.getElementById(id).style.display = "block";
}

function closeModal(id) {
    document.getElementById(id).style.display = "none";
}

// Close modal if user clicks outside the box
window.onclick = function(event) {
    if (event.target.className === 'custom-modal') {
        event.target.style.display = "none";
    }
}

// FAQ Toggle Function
    function toggleFaq(element) {
        const item = element.parentElement;
        item.classList.toggle('active');
        
        // Toggle icon between plus and minus
        const icon = element.querySelector('i');
        if (item.classList.contains('active')) {
            icon.classList.replace('fa-plus', 'fa-minus');
        } else {
            icon.classList.replace('fa-minus', 'fa-plus');
        }
    }