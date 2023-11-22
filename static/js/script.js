// static/script.js

function toggleMenu() {
    var menuContent = document.getElementById('menu');
    if (menuContent.style.transform === 'translateX(0%)') {
        menuContent.style.transform = 'translateX(100%)';
    } else {
        menuContent.style.transform = 'translateX(0%)';
    }
}
