function showMessageResponse(message, category, animationIn = "animate__bounceIn", animationOut = "animate__fadeOut") {
    const symbolPath = category => {
        const checkCircle = "M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z";
        const infoFill = "M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2z";
        const exclamationTriangleFill = "M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z";

        return {
            "primary": exclamationTriangleFill,
            "success": checkCircle,
            "danger": exclamationTriangleFill,
            "warning": infoFill,
            "info": infoFill
        }[category];
    };

    const createExternalDiv = () => {
        const externalDiv = document.createElement("div");
        externalDiv.style.fontSize = "small";
        externalDiv.style.bottom = "0px";
        externalDiv.style.position = "fixed";
        externalDiv.style.left = "50%";
        externalDiv.style.transform = "translate(-50%)";
        return externalDiv;
    };

    const createChildDiv = () => {
        const calculateWidth = (windowWidth) => { return windowWidth <= 400 ? `${windowWidth - 40}px` : "max-content"; }

        const childDiv = document.createElement("div");
        childDiv.classList.add(
            "message-response", "alert", `alert-${category}`, 
            "d-flex", "align-items-center", "justify-content-center", 
            "border-0", "px-4", "rounded-pill", "shadow-sm", 
            "animate__animated", animationIn
        );
        childDiv.setAttribute("role", "alert");
        childDiv.style.width = calculateWidth(window.innerWidth);
        window.addEventListener("resize", () => { childDiv.style.width = calculateWidth(window.innerWidth); });
        childDiv.innerHTML = `
            <svg class="me-2" width="14px" height="14px" viewBox="0 0 16 16" style="min-width: 14px; min-height=14px;">
                <path d="${symbolPath(category)}" />
            </svg>
            ${message}
        `;
        return childDiv;
    };

    const removePreviousResponse = () => {
        const previousResponse = document.querySelector(".message-response");
        if (previousResponse) { previousResponse.remove(); }
    };

    const removeCurrentResponse = (externalDiv, childDiv) => {
        childDiv.classList.remove(animationIn);
        childDiv.classList.add(animationOut);
        setTimeout(() => externalDiv.remove(), 1000);
    };

    removePreviousResponse();
    const externalDiv = createExternalDiv();
    const childDiv = createChildDiv();
    externalDiv.appendChild(childDiv);
    setTimeout(() => removeCurrentResponse(externalDiv, childDiv), 7 * 1000);
    document.querySelector("script").insertAdjacentElement("beforebegin", externalDiv);
}


function handleJsonResponse(data) {
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
            handleJsonResponse(data);
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
            handleJsonResponse(data);
        } catch (error) {
            console.error(error);
        }
    });
}


function handleFlashMessage() {
    const flashMessage = document.querySelector(".flash");

    if (flashMessage) {
        document.addEventListener("DOMContentLoaded", () => { 
            showMessageResponse(flashMessage.dataset.message, flashMessage.dataset.category);
        });

        flashMessage.remove();
    }
}
