/**
 * Flask MVC - marcusxyz
 * https://github.com/marcuxyz/mvc-flask
 */

const form = document.querySelector('form');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(form)
    const formAction = form.getAttribute('action');
    const formMethod = form.getAttribute('method').toLowerCase();

    if (formMethod == 'put' || formMethod == 'delete') {
        const response = await fetch(formAction, {
            method: formMethod, body: formData
        })

        if (response.redirected) {
            window.location.href = response.url
        }
    }
})