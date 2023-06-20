let menuList = document.querySelectorAll('.drinks-list-item');

for (let menuListItem of menuList) {
    if(menuListItem.contains(menuListItem.querySelector('.amount-button'))) {
        for (let buttonToCart of menuListItem.querySelectorAll('.button-to-cart')) {
            buttonToCart.style.display = "none";
        }
    }
    else {
        let count = 0;
        for (let buttonToCart of menuListItem.querySelectorAll('.button-to-cart')) {
            count++;
            if (count === menuListItem.querySelectorAll('.button-to-cart').length) {
                break
            }
            buttonToCart.style.display = "none";
        }
    }
}
