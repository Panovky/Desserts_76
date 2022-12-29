document.addEventListener("DOMContentLoaded", onDOMReady);

function onDOMReady() {
    window.addEventListener('scroll', onWindowScroll)

    let menu = document.getElementById('navigation');
    let logo = document.getElementById('link_logo');

    function onWindowScroll() {
        if(window.document.scrollingElement.scrollTop > 100){
            menu.classList.add("fixed");
            menu.style.padding = '15px 0px';
            menu.style.zIndex = '1000';
            logo.style.display = 'none';
        }
        else {
            menu.classList.remove("fixed")
            menu.style.padding = '8px 0px';
            menu.style.zIndex = '1000';
            logo.style.display = 'block';
        }
    }
}

let mySwiper = new Swiper ('.about_foto-aside', {
    loop: true,
    navigation: {
        nextEl: '.btn-swiper-next',
        prevEl: '.btn-swiper-prev',
    },
})


let popupBg = document.querySelector('.popup__bg'); // Фон попап окна
let popup = document.querySelector('.popup'); // Само окно
let openPopupButtons = document.querySelectorAll('.open-popup'); // Кнопки для показа окна
let closePopupButton = document.querySelector('.close-popup'); // Кнопка для скрытия окна

openPopupButtons.forEach((button) => { // Перебираем все кнопки
    button.addEventListener('click', (e) => { // Для каждой вешаем обработчик событий на клик
        e.preventDefault(); // Предотвращаем дефолтное поведение браузера
        popupBg.classList.add('active'); // Добавляем класс 'active' для фона
        popup.classList.add('active'); // И для самого окна
    })
});

closePopupButton.addEventListener('click',() => { // Вешаем обработчик на крестик
    popupBg.classList.remove('active'); // Убираем активный класс с фона
    popup.classList.remove('active'); // И с окна
});

document.addEventListener('click', (e) => { // Вешаем обработчик на весь документ
    if(e.target === popupBg) { // Если цель клика - фот, то:
        popupBg.classList.remove('active'); // Убираем активный класс с фона
        popup.classList.remove('active'); // И с окна
    }
});