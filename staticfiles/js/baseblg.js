// alert("hello manish");
var checked = document.querySelector(".checkbox");
var first = document.querySelector(".blg-navbar");
var second = document.querySelector(".user-name-container");
var third = document.querySelector(".contact-btn");
var btn = document.querySelector(".btn-1");


function input() {
    if (checked.checked) {
        first.style.display = "flex";
        third.style.display = "flex";
        if (btn.textContent != 'Sign-In') {
            console.log("not log-in");
            second.style.display = "flex";
        }
    }
    if (!checked.checked) {
        first.style.display = "none";
        third.style.display = "none";
        if (btn.textContent != 'Sign-In') {
            second.style.display = "none";
        }

    }
}