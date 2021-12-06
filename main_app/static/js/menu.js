document.addEventListener('DOMContentLoaded',function(){

const navButton = document.getElementById("nav-button")
const menu = document.getElementsByClassName("nav-menu")[0]

navButton.addEventListener("click", () => {
    navButton.classList.toggle("open")
    menu.classList.toggle("nav-menu-active")
})
})