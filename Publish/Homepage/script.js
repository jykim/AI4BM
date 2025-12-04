// Navigation Logic
function renderNavigation() {
    const nav = document.querySelector('.main-nav');
    if (!nav) return;

    const path = window.location.pathname;
    const page = path.split('/').pop() || 'index.html';
    const isEnglish = page === 'index_en.html';

    const links = [
        { name: 'Theory', href: 'theory.html' },
        { name: 'Software', href: 'software.html' },
        { name: 'Skills', href: 'skills.html' },
        { name: 'Resources', href: 'resources.html' }
    ];

    const logoHref = isEnglish ? 'index_en.html' : 'index.html';
    
    let langToggle = '';
    if (page === 'index.html' || page === '') {
        langToggle = '<a href="index_en.html" class="lang-toggle-nav">English</a>';
    } else if (page === 'index_en.html') {
        langToggle = '<a href="index.html" class="lang-toggle-nav">한국어</a>';
    }

    const linksHtml = links.map(link => {
        let activeClass = '';
        if (page === link.href) {
            activeClass = ' active';
        } else if (link.name === 'Theory' && (page.startsWith('theory'))) {
            activeClass = ' active';
        } else if (link.name === 'Software' && (page === 'orchestrator.html')) {
            activeClass = ' active';
        }
        return `<a href="${link.href}" class="nav-link${activeClass}">${link.name}</a>`;
    }).join('\n                    ');

    nav.innerHTML = `
        <div class="container">
            <div class="nav-left">
                <a href="${logoHref}" class="nav-logo">AI for Better Me</a>
                <div class="nav-links">
                    ${linksHtml}
                </div>
            </div>
            ${langToggle}
        </div>
    `;
}

// Run navigation render immediately
renderNavigation();

const canvas = document.getElementById('brain-canvas');
const ctx = canvas.getContext('2d');

let width, height;
let particles = [];

// Configuration
const particleCount = 800; // Increased for density
const connectionDistance = 60; // Reduced for tighter clusters
const mouseDistance = 150;

// Resize handling
function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
    init(); // Re-initialize on resize to position correctly
}

window.addEventListener('resize', resize);

// Mouse interaction
const mouse = { x: null, y: null };
window.addEventListener('mousemove', (e) => {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
});
window.addEventListener('mouseleave', () => {
    mouse.x = null;
    mouse.y = null;
});

// Particle Class
class Particle {
    constructor(type) {
        this.type = type; // 'brain' or 'ai'
        this.size = Math.random() * 1.5 + 0.5;
        this.baseX = 0;
        this.baseY = 0;
        this.x = 0;
        this.y = 0;
        this.vx = (Math.random() - 0.5) * 0.2;
        this.vy = (Math.random() - 0.5) * 0.2;

        this.setPosition();
        this.x = this.baseX;
        this.y = this.baseY;

        // Colors
        if (this.type === 'brain') {
            // Pinkish/Purple for brain
            this.color = `rgba(236, 72, 153, ${Math.random() * 0.5 + 0.2})`;
        } else {
            // Blue/Cyan for AI
            this.color = `rgba(59, 130, 246, ${Math.random() * 0.5 + 0.2})`;
        }
    }

    setPosition() {
        if (this.type === 'brain') {
            // Brain Shape: Elliptical cluster on the left
            // Main ellipse
            const angle = Math.random() * Math.PI * 2;
            const radius = Math.sqrt(Math.random()) * (Math.min(width, height) * 0.25);
            // Flatten slightly to look more like a brain side view
            this.baseX = (width * 0.3) + radius * Math.cos(angle) * 0.8;
            this.baseY = (height * 0.5) + radius * Math.sin(angle);

            // Add some "lobes"
            if (Math.random() > 0.7) {
                this.baseX += (Math.random() - 0.5) * 50;
                this.baseY += (Math.random() - 0.5) * 50;
            }
        } else {
            // AI Shape: Structured grid/network on the right
            // Distributed in a wider area
            this.baseX = (width * 0.7) + (Math.random() - 0.5) * (width * 0.4);
            this.baseY = (height * 0.5) + (Math.random() - 0.5) * (height * 0.8);
        }
    }

    update() {
        // Gentle floating
        this.x += this.vx;
        this.y += this.vy;

        // Tether to base position
        const dx = this.baseX - this.x;
        const dy = this.baseY - this.y;
        this.x += dx * 0.01;
        this.y += dy * 0.01;

        // Mouse interaction
        if (mouse.x != null) {
            const dx = mouse.x - this.x;
            const dy = mouse.y - this.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            if (distance < mouseDistance) {
                const forceDirectionX = dx / distance;
                const forceDirectionY = dy / distance;
                const force = (mouseDistance - distance) / mouseDistance;
                const directionX = forceDirectionX * force * 2;
                const directionY = forceDirectionY * force * 2;
                this.x -= directionX; // Push away
                this.y -= directionY;
            }
        }
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.fill();
    }
}

// Initialize particles
function init() {
    // resize(); // Removed to prevent infinite recursion: init() -> resize() -> init()
    particles = [];

    // Create Brain particles
    for (let i = 0; i < particleCount * 0.6; i++) {
        particles.push(new Particle('brain'));
    }

    // Create AI particles
    for (let i = 0; i < particleCount * 0.4; i++) {
        particles.push(new Particle('ai'));
    }
}

// Animation Loop
function animate() {
    ctx.clearRect(0, 0, width, height);

    for (let i = 0; i < particles.length; i++) {
        particles[i].update();
        particles[i].draw();

        // Draw connections
        // Optimization: Only check nearby particles in the array (approximate spatial locality)
        // or just limit the inner loop
        for (let j = i; j < particles.length; j++) {
            const dx = particles[i].x - particles[j].x;
            const dy = particles[i].y - particles[j].y;

            // Quick check for distance (squared to avoid sqrt)
            if (Math.abs(dx) > connectionDistance || Math.abs(dy) > connectionDistance) continue;

            const distanceSq = dx * dx + dy * dy;

            if (distanceSq < connectionDistance * connectionDistance) {
                ctx.beginPath();
                const distance = Math.sqrt(distanceSq);

                // Gradient connection
                const gradient = ctx.createLinearGradient(particles[i].x, particles[i].y, particles[j].x, particles[j].y);
                gradient.addColorStop(0, particles[i].color);
                gradient.addColorStop(1, particles[j].color);

                ctx.strokeStyle = gradient;
                ctx.lineWidth = 0.5;
                ctx.globalAlpha = 1 - distance / connectionDistance;
                ctx.moveTo(particles[i].x, particles[i].y);
                ctx.lineTo(particles[j].x, particles[j].y);
                ctx.stroke();
                ctx.globalAlpha = 1;
            }
        }
    }

    requestAnimationFrame(animate);
}

// Initial setup
width = canvas.width = window.innerWidth;
height = canvas.height = window.innerHeight;
init();
animate();
