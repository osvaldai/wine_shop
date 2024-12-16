// products/static/products/js/scripts.js

// Плавная анимация появления элементов при скроллинге
window.addEventListener('scroll', function() {
    const elements = document.querySelectorAll('.product-showcase, .hero-section, .wine-history');
    elements.forEach(element => {
        const position = element.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        if (position < windowHeight - 100) {
            element.classList.add('visible');
        }
    });
});

// Добавление класса для анимации появления
document.addEventListener('DOMContentLoaded', function() {
    const elements = document.querySelectorAll('.product-showcase, .hero-section, .wine-history');
    elements.forEach(element => {
        element.classList.add('hidden');  // Исходное состояние - скрыто
    });
});

/* CSS для скрытых и видимых элементов */
const style = document.createElement('style');
style.innerHTML = `
.hidden {
    opacity: 0;
    transform: translateY(50px);
    transition: all 0.6s ease-out;
}
.visible {
    opacity: 1;
    transform: translateY(0);
}
`;
document.head.appendChild(style);