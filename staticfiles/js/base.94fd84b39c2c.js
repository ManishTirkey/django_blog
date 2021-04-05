// console.log("hello ");
/* transform: translateY(-100%); */



var si_body = document.querySelector(".sign-in-bg");
var re_body = document.querySelector(".register-bg");
// var property = document.styleSheets[0].cssRules[20].style;

function sign_In() {
    // property.removeProperty('transform');
    si_body.style.transform = "translateY(0)";
}

function si_hide() {
    si_body.style.transform = "translateY(-300%)";
}

function register() {
    // property.removeProperty('transform');
    re_body.style.transform = "translateY(0)";
}

function re_hide() {
    re_body.style.transform = "translateY(-300%)";
}