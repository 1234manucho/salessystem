// Select the element to animate
const box = document.querySelector('app.py.box');

// Add animation using JavaScript
function animateBox() {
    box.style.transition = 'transform 2s ease-in-out';
    box.style.transform = 'translateX(300px)';
}

// Trigger animation on button click
document.querySelector('.animate-btn').addEventListener('click', animateBox);