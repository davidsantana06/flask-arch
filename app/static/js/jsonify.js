function handleResponseData(data) {
    if (data.redirect) {
        window.location.replace(data.redirect);
    } else {
        showMessageResponse(data.message, data.category);
    }
}


function jsonifyForm(form) {
    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        try {
            const response = await fetch(form.dataset.action, {
                method: form.dataset.method,
                body: new FormData(form)
            });
            const data = await response.json();
            handleResponseData(data);
        } catch (error) {
            console.error(error);
        }
    });
}


function jsonifyButton(button) {
    button.addEventListener("click", async (event) => {
        event.preventDefault();

        try {
            const response = await fetch(button.dataset.action, {
                method: button.dataset.method,
                headers: { "X-CSRFToken": button.dataset.csrf }
            });
            const data = await response.json();
            handleResponseData(data);
        } catch (error) {
            console.error(error);
        }
    });
}
