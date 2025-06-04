document.addEventListener('DOMContentLoaded', function() {
    // Initialize file inputs
    const fileInputs = document.querySelectorAll('input[type="file"]');
    
    fileInputs.forEach(fileInput => {
        const fileLabel = fileInput.nextElementSibling;
        const originalLabelText = fileLabel.innerHTML;

        function handleFile(file) {
            if (file) {
                const dataTransfer = new DataTransfer();
                dataTransfer.items.add(file);
                fileInput.files = dataTransfer.files;

                fileLabel.innerHTML = originalLabelText + ' - ' + file.name;
                fileLabel.classList.add('file-selected');
                setTimeout(() => {
                    fileLabel.classList.remove('file-selected');
                }, 3000);
            }
        }

        fileInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            handleFile(file);
        });

        // Drag and drop events
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            fileLabel.addEventListener(eventName, preventDefaults, false);
        });

        ['dragenter', 'dragover'].forEach(eventName => {
            fileLabel.addEventListener(eventName, highlight, false);
        });

        ['dragleave', 'drop'].forEach(eventName => {
            fileLabel.addEventListener(eventName, unhighlight, false);
        });

        fileLabel.addEventListener('drop', handleDrop, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    function highlight(e) {
        e.target.classList.add('dragover');
    }

    function unhighlight(e) {
        e.target.classList.remove('dragover');
    }

    function handleDrop(e) {
        const file = e.dataTransfer.files[0];
        if (file && file.type === 'application/pdf') {
            handleFile(file);
        }
    }
});