function toggleMenu() {
    var menu = document.getElementById('menu');
    if (menu.style.right === '-250px' || menu.style.right === '') {
        menu.style.right = '0';
        menu.style.display = 'block';
    } else {
        menu.style.right = '-250px';
        menu.style.display = 'none';
    }
}
