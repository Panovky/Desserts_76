document.addEventListener("DOMContentLoaded", onDOMReady);

function onDOMReady() {
    window.addEventListener('scroll', onWindowScroll)

    let menu = document.getElementById('navigation');
    let logo = document.getElementById('link_logo');

    function onWindowScroll() {
        if(window.document.scrollingElement.scrollTop > 100){
            menu.classList.add("fixed");
            menu.style.padding = '15px 0px';
            logo.style.display = 'none';
        }
        else {
            menu.classList.remove("fixed")
            menu.style.padding = '5px 0px';
            logo.style.display = 'block';
        }
    }
}
