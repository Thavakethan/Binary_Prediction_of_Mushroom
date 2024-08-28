document.getElementById('upload-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData();
    const fileInput = document.getElementById('file-input');
    formData.append('file', fileInput.files[0]);

    fetch('http://localhost:5000/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const downloadLink = document.getElementById('download-link');
        downloadLink.href = data.fileUrl;
        downloadLink.style.display = 'inline';
    })
    .catch(error => console.error('Error:', error));
});
