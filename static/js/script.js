function toggleMenu() {
    var menu = document.getElementById('menu');
    if (menu.style.transform === 'translateX(0%)') {
        menu.style.transform = 'translateX(100%)';
    } else {
        menu.style.transform = 'translateX(0%)';
    }
}

function resizeTextarea() {
    var elements = document.getElementsByClassName("Experience_details");
  
    // 모든 요소에 대해 루프 실행
    for (var i = 0; i < elements.length; i++) {
      var textarea = elements[i];
      textarea.style.height = "auto"; // 높이를 초기화
  
      // 실제 높이를 계산하고 설정
      textarea.style.height = (textarea.scrollHeight) + "px";
    }
  }
  window.onload = resizeTextarea;

