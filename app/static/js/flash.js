const flashMessage = document.querySelector(".flash");

if (flashMessage) {
    document.addEventListener("DOMContentLoaded", () => { 
        showMessageResponse(flashMessage.dataset.message, flashMessage.dataset.category);
    });

    flashMessage.remove();
}
