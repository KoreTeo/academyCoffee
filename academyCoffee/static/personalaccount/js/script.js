let modalChangeName = document.querySelector(".modal-change-name");
let buttonModalChangeName = document.querySelector("#modalChangeName");
let exitName = document.querySelector(".close-modal-name");

buttonModalChangeName.onclick = function () {
    modalChangeName.style.display = "block";
}

exitName.onclick = function () {
    modalChangeName.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modalChangeName) {
        modalChangeName.style.display = "none";
    }
}



let modalChangeDate = document.querySelector(".modal-change-date");
let buttonModalChangeDate = document.querySelector("#modalChangeDate");
let exitDate = document.querySelector(".close-modal-date");

buttonModalChangeDate.onclick = function () {
    modalChangeDate.style.display = "block";
}

exitDate.onclick = function () {
    modalChangeDate.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modalChangeDate) {
        modalChangeDate.style.display = "none";
    }
}



let modalChangeRegion = document.querySelector(".modal-change-region");
let buttonModalChangeRegion = document.querySelector("#modalChangeRegion");
let exitRegion = document.querySelector(".close-modal-region");

buttonModalChangeRegion.onclick = function () {
    modalChangeRegion.style.display = "block";
}

exitRegion.onclick = function () {
    modalChangeRegion.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modalChangeRegion) {
        modalChangeRegion.style.display = "none";
    }
}



let modalChangeNumber = document.querySelector(".modal-change-number");
let buttonModalChangeNumber = document.querySelector("#modalChangeNumber");
let exitNumber = document.querySelector(".close-modal-number");

buttonModalChangeNumber.onclick = function () {
    modalChangeNumber.style.display = "block";
}

exitNumber.onclick = function () {
    modalChangeNumber.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modalChangeNumber) {
        modalChangeNumber.style.display = "none";
    }
}