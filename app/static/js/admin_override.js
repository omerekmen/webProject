// admin_override.js
(function ($) {
    $(document).ready(function () {
        // Find the "Add Another" link and override its behavior
        $('a.add-another').on('click', function (e) {
            e.preventDefault(); // Prevent the default behavior (opening a new tab)
            var url = $(this).attr('href'); // Get the URL of the related object creation page
            if (url) {
                // Open the related object creation page in the same tab
                window.location.href = url;
            }
        });
    });
})(django.jQuery);
