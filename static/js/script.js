function toggleMenu() {
    var menu = document.getElementById('menu');
    if (menu.style.transform === 'translateX(0%)') {
        menu.style.transform = 'translateX(100%)';
    } else {
        menu.style.transform = 'translateX(0%)';
    }
}
