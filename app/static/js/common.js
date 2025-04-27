async function handleFormSubmit(event) {
    event.preventDefault();
    
    const form = event.target;
    const formData = new FormData(form);
    const jsonData = {};

    formData.forEach((value, key) => {
        jsonData[key] = value;
    });

    try {
        const response = await fetch(form.action, {
            method: form.method || 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonData)
        });

        if (response.redirected) {
            window.location.href = response.url;
            return;
        }

        const data = await response.json();

        if (response.ok) {
            return data;
        } else {
            throw new Error(data.message || 'Form submission failed');
        }
    } catch (error) {
        console.error('Error submitting form:', error);
        throw error;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const ajaxForms = document.querySelectorAll('form.ajax-form');

    ajaxForms.forEach(form => {
        form.addEventListener('submit', async (e) => {
            try {
                const data = await handleFormSubmit(e);
                console.log('Form submitted successfully:', data);
            } catch (error) {
                console.error('Form submission error:', error);
            }
        });
    });
});
