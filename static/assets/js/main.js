/**
 * PORTFOLIO ULTRA-MODERNE - DONALDO ZOUBERY
 * JavaScript moderne avec animations avancées
 */

(function() {
    'use strict';

    // ========================================
    // CONFIGURATION GLOBALE
    // ========================================
    const CONFIG = {
        animationDuration: 1000,
        scrollOffset: 100,
        typingSpeed: 100,
        particlesCount: 50,
        floatingSpeed: 6
    };

    // ========================================
    // UTILITAIRES
    // ========================================
    const $ = (selector, all = false) => {
        if (all) {
            return [...document.querySelectorAll(selector)];
        }
        return document.querySelector(selector);
    };

    const debounce = (func, wait) => {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    };

    const throttle = (func, limit) => {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    };

    // ========================================
    // ANIMATIONS DE COMPTAGE
    // ========================================
    class CounterAnimation {
        constructor(element, target, duration = 2000) {
            this.element = element;
            this.target = target;
            this.duration = duration;
            this.start = 0;
            this.increment = target / (duration / 16);
            this.current = 0;
        }

        start() {
            const animate = () => {
                this.current += this.increment;
                if (this.current >= this.target) {
                    this.current = this.target;
                    this.element.textContent = this.target;
                    return;
                }
                this.element.textContent = Math.floor(this.current);
                requestAnimationFrame(animate);
            };
            animate();
        }
    }

    // ========================================
    // ANIMATION DE TEXTE TYPEWRITER
    // ========================================
    class TypewriterAnimation {
        constructor(element, strings, speed = 100) {
            this.element = element;
            this.strings = strings;
            this.speed = speed;
            this.currentStringIndex = 0;
            this.currentCharIndex = 0;
            this.isDeleting = false;
            this.typeSpeed = speed;
        }

        start() {
            this.type();
        }

        type() {
            const currentString = this.strings[this.currentStringIndex];
            
            if (this.isDeleting) {
                this.element.textContent = currentString.substring(0, this.currentCharIndex - 1);
                this.currentCharIndex--;
                this.typeSpeed = this.speed / 2;
            } else {
                this.element.textContent = currentString.substring(0, this.currentCharIndex + 1);
                this.currentCharIndex++;
                this.typeSpeed = this.speed;
            }

            if (!this.isDeleting && this.currentCharIndex === currentString.length) {
                this.typeSpeed = 2000; // Pause avant de commencer à effacer
                this.isDeleting = true;
            } else if (this.isDeleting && this.currentCharIndex === 0) {
                this.isDeleting = false;
                this.currentStringIndex = (this.currentStringIndex + 1) % this.strings.length;
                this.typeSpeed = 500; // Pause avant de commencer à taper
            }

            setTimeout(() => this.type(), this.typeSpeed);
        }
    }

    // ========================================
    // PARTICULES FLOTTANTES
    // ========================================
    class ParticleSystem {
        constructor(container) {
            this.container = container;
            this.particles = [];
            this.init();
        }

        init() {
            for (let i = 0; i < CONFIG.particlesCount; i++) {
                this.createParticle();
            }
            this.animate();
        }

        createParticle() {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.cssText = `
                position: absolute;
                width: 2px;
                height: 2px;
                background: rgba(99, 102, 241, 0.5);
                border-radius: 50%;
                pointer-events: none;
                left: ${Math.random() * 100}%;
                top: ${Math.random() * 100}%;
                animation: float ${CONFIG.floatingSpeed + Math.random() * 4}s linear infinite;
            `;
            this.container.appendChild(particle);
            this.particles.push(particle);
        }

        animate() {
            this.particles.forEach(particle => {
                const x = Math.random() * window.innerWidth;
                const y = Math.random() * window.innerHeight;
                particle.style.left = x + 'px';
                particle.style.top = y + 'px';
            });
        }
    }

    // ========================================
    // NAVIGATION SMOOTH SCROLL
    // ========================================
    class SmoothScroll {
        constructor() {
            this.init();
        }

        init() {
            $('a[href^="#"]', true).forEach(link => {
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    const targetId = link.getAttribute('href');
                    const targetElement = $(targetId);
                    
                    if (targetElement) {
                        const offsetTop = targetElement.offsetTop - CONFIG.scrollOffset;
                        window.scrollTo({
                            top: offsetTop,
                            behavior: 'smooth'
                        });
                    }
                });
            });
        }
    }

    // ========================================
    // NAVIGATION STICKY
    // ========================================
    class StickyNavigation {
        constructor() {
            this.navbar = $('#navbar');
            this.header = $('#header');
            this.init();
        }

        init() {
            if (!this.navbar) return;

            window.addEventListener('scroll', throttle(() => {
                const scrollTop = window.pageYOffset;
                
                if (scrollTop > 100) {
                    this.navbar.classList.add('navbar-scrolled');
                    this.header?.classList.add('header-top');
                } else {
                    this.navbar.classList.remove('navbar-scrolled');
                    this.header?.classList.remove('header-top');
                }
            }, 100));
        }
    }

    // ========================================
    // ANIMATIONS AU SCROLL
    // ========================================
    class ScrollAnimations {
        constructor() {
            this.elements = $('[data-aos]', true);
            this.init();
        }

        init() {
            if (this.elements.length === 0) return;

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('aos-animate');
                        this.animateElement(entry.target);
                    }
                });
            }, {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            });

            this.elements.forEach(element => {
                observer.observe(element);
            });
        }

        animateElement(element) {
            const animationType = element.dataset.aos;
            const delay = element.dataset.aosDelay || 0;

            setTimeout(() => {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0) translateX(0) scale(1)';
            }, delay);
        }
    }

    // ========================================
    // FILTRE PORTFOLIO
    // ========================================
    class PortfolioFilter {
        constructor() {
            this.container = $('.portfolio-container');
            this.filters = $('#portfolio-flters li', true);
            this.items = $('.portfolio-item', true);
            this.init();
        }

        init() {
            if (!this.container) return;

            this.filters.forEach(filter => {
                filter.addEventListener('click', (e) => {
                    e.preventDefault();
                    
                    // Mettre à jour les classes actives
                    this.filters.forEach(f => f.classList.remove('filter-active'));
                    filter.classList.add('filter-active');
                    
                    // Filtrer les éléments
                    const filterValue = filter.dataset.filter;
                    this.filterItems(filterValue);
                });
            });
        }

        filterItems(filter) {
            this.items.forEach(item => {
                if (filter === '*' || item.classList.contains(filter)) {
                    item.style.display = 'block';
                    item.style.animation = 'fadeInUp 0.5s ease-out';
                } else {
                    item.style.display = 'none';
                }
            });
        }
    }

    // ========================================
    // FORMULAIRE DE CONTACT
    // ========================================
    class ContactForm {
        constructor() {
            this.form = $('#contactme_form');
            this.submitBtn = $('#recaptcha-submit');
            this.init();
        }

        init() {
            if (!this.form) return;

            this.form.addEventListener('submit', (e) => {
                e.preventDefault();
                this.handleSubmit();
            });
        }

        async handleSubmit() {
            const formData = new FormData(this.form);
            const submitBtn = this.submitBtn;
            
            // Désactiver le bouton
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="loading"></span> Envoi en cours...';

            try {
                const response = await fetch(this.form.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-CSRFToken': this.getCSRFToken()
                    }
                });

                const data = await response.json();

                if (data.status === 'success') {
                    this.showMessage('Votre message a été envoyé avec succès!', 'success');
                    this.form.reset();
                } else {
                    this.showMessage('Erreur lors de l\'envoi du message.', 'error');
                }
            } catch (error) {
                this.showMessage('Erreur de connexion. Veuillez réessayer.', 'error');
            } finally {
                submitBtn.disabled = false;
                submitBtn.innerHTML = 'Envoyer le Message';
            }
        }

        getCSRFToken() {
            return $('input[name="csrfmiddlewaretoken"]').value;
        }

        showMessage(message, type) {
            const messageDiv = document.createElement('div');
            messageDiv.className = `alert alert-${type}`;
            messageDiv.textContent = message;
            messageDiv.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                padding: 15px 20px;
                border-radius: 5px;
                color: white;
                z-index: 9999;
                animation: slideInRight 0.3s ease-out;
                background: ${type === 'success' ? '#10b981' : '#ef4444'};
            `;

            document.body.appendChild(messageDiv);

            setTimeout(() => {
                messageDiv.style.animation = 'slideOutRight 0.3s ease-out';
                setTimeout(() => messageDiv.remove(), 300);
            }, 3000);
        }
    }

    // ========================================
    // BOUTON BACK TO TOP
    // ========================================
    class BackToTop {
        constructor() {
            this.button = $('#back-to-top');
            this.init();
        }

        init() {
            if (!this.button) return;

            window.addEventListener('scroll', throttle(() => {
                if (window.pageYOffset > 300) {
                    this.button.classList.add('show');
                } else {
                    this.button.classList.remove('show');
                }
            }, 100));

            this.button.addEventListener('click', (e) => {
                e.preventDefault();
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
        }
    }

    // ========================================
    // ANIMATIONS DE PROGRESSION
    // ========================================
    class ProgressAnimations {
        constructor() {
            this.bars = $('.progress-bar', true);
            this.init();
        }

        init() {
            if (this.bars.length === 0) return;

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const bar = entry.target;
                        const width = bar.dataset.width;
                        this.animateBar(bar, width);
                    }
                });
            });

            this.bars.forEach(bar => {
                observer.observe(bar);
            });
        }

        animateBar(bar, width) {
            let currentWidth = 0;
            const increment = width / 50;
            
            const animate = () => {
                currentWidth += increment;
                if (currentWidth >= width) {
                    currentWidth = width;
                }
                bar.style.width = currentWidth + '%';
                
                if (currentWidth < width) {
                    requestAnimationFrame(animate);
                }
            };
            
            animate();
        }
    }

    // ========================================
    // THEME TOGGLE
    // ========================================
    class ThemeToggle {
        constructor() {
            this.toggleBtn = $('#theme-toggle');
            this.body = document.body;
            this.init();
        }

        init() {
            if (!this.toggleBtn) return;

            // Charger le thème sauvegardé
            const savedTheme = localStorage.getItem('theme') || 'dark';
            this.setTheme(savedTheme);

            this.toggleBtn.addEventListener('click', () => {
                const currentTheme = this.body.classList.contains('dark-theme') ? 'dark' : 'light';
                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                this.setTheme(newTheme);
            });
        }

        setTheme(theme) {
            if (theme === 'dark') {
                this.body.classList.add('dark-theme');
                this.toggleBtn?.classList.add('active');
            } else {
                this.body.classList.remove('dark-theme');
                this.toggleBtn?.classList.remove('active');
            }
            localStorage.setItem('theme', theme);
        }
    }

    // ========================================
    // INITIALISATION
    // ========================================
    class App {
        constructor() {
            this.init();
        }

        init() {
            // Attendre que le DOM soit chargé
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', () => this.start());
            } else {
                this.start();
            }
        }

        start() {
            // Initialiser les animations de comptage
            $('.stat-number', true).forEach(element => {
                const target = parseInt(element.dataset.count);
                if (target) {
                    new CounterAnimation(element, target).start();
                }
            });

            // Initialiser l'animation typewriter
            const typingElement = $('.typing-text');
            if (typingElement) {
                const strings = JSON.parse(typingElement.dataset.strings || '[]');
                new TypewriterAnimation(typingElement, strings, CONFIG.typingSpeed).start();
            }

            // Initialiser les particules
            const particlesContainer = $('#particles-js');
            if (particlesContainer) {
                new ParticleSystem(particlesContainer);
            }

            // Initialiser les autres composants
            new SmoothScroll();
            new StickyNavigation();
            new ScrollAnimations();
            new PortfolioFilter();
            new ContactForm();
            new BackToTop();
            new ProgressAnimations();
            new ThemeToggle();

            // Initialiser AOS si disponible
            if (typeof AOS !== 'undefined') {
                AOS.init({
                    duration: CONFIG.animationDuration,
                    easing: 'ease-in-out',
                    once: true,
                    mirror: false
                });
            }

            console.log('🚀 Portfolio ultra-moderne initialisé avec succès!');
        }
    }

    // Démarrer l'application
    new App();

    // ========================================
    // ANIMATIONS CSS SUPPLÉMENTAIRES
    // ========================================
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideInRight {
            from {
                transform: translateX(100%);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }

        @keyframes slideOutRight {
            from {
                transform: translateX(0);
                opacity: 1;
            }
            to {
                transform: translateX(100%);
                opacity: 0;
            }
        }

        .navbar-scrolled {
            background: rgba(15, 15, 35, 0.95) !important;
            backdrop-filter: blur(10px);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        }

        .particle {
            animation: float 6s linear infinite;
        }

        @keyframes float {
            0%, 100% {
                transform: translateY(0px) rotate(0deg);
            }
            50% {
                transform: translateY(-20px) rotate(180deg);
            }
        }

        .aos-animate {
            opacity: 1 !important;
            transform: translateY(0) translateX(0) scale(1) !important;
        }

        [data-aos] {
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.6s ease-out;
        }

        [data-aos="fade-left"] {
            transform: translateX(-30px);
        }

        [data-aos="fade-right"] {
            transform: translateX(30px);
        }

        [data-aos="scale-in"] {
            transform: scale(0.9);
        }
    `;
    document.head.appendChild(style);

})();