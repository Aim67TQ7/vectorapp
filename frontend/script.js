document.getElementById('uploadForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    let formData = new FormData();
    formData.append('file', document.getElementById('file').files[0]);

    try {
        const response = await fetch('http://localhost:5000/upload', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        document.getElementById('responseMessage').innerText = result.message || result.error;
    } catch (error) {
        document.getElementById('responseMessage').innerText = "An error occurred while uploading.";
    }
});
