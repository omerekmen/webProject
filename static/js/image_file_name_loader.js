$(document).ready(function() {
    $(document).on('change', '#validatedCustomFile', function() {
        updateFileName(this);
    });

    function updateFileName(input) {
        var fileName = input.files[0].name;
        var label = document.querySelector('label[for="' + input.id + '"]');
        var fni = document.getElementById("file-name-input")
        fni.value = 'Yüklenen Dosya: ' + fileName;
    }
});

