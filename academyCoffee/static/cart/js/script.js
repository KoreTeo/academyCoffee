let modalChangePayment = document.querySelector(".modal-change-payment");
let buttonModalChangePayment = document.querySelector("#modalChangePayment");
let exitPayment = document.querySelector("#close-modal-payment");

buttonModalChangePayment.onclick = function () {
    modalChangePayment.style.display = "block";
}

exitPayment.onclick = function () {
    modalChangePayment.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modalChangePayment) {
        modalChangePayment.style.display = "none";
    }
}
