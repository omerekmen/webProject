$(document).ready(function () {
    // Open popup when the "Open Popup" button is clicked
    $('.open-popup-button').on('click', function (e) {
        e.preventDefault();

        var id = $(this).data('popup-id');
        var title = $(this).data('popup-title');
        var content = $(this).data('popup-content');
        var buttonName = $(this).data('popup-button-name');
        var buttonClass = $(this).data('popup-button-class');
        var checkstatuspopup = $(this).data('popup-warehouse-status');
        var formactionurl = $(this).data('popup-action-url');
        var csrftoken = $(this).data('popup-csrf-token');


        var popup_status_true = `
        <div class="newsletter-popup newsletter-pop3" id="${id}">
            <div class="newsletter-content">
                <!-- Popup Title -->
                <h4 class="text-uppercase text-dark"><span class="text-dark">${title}</span></h4>

                <hr class="product-divider">
                
                <!-- Popup Content -->
                <p class="text-grey">
                    ${content}
                </p>
                <div class="col-sm-12">
                    
                    <div class="row" style="margin-bottom:-4rem;">
                        <div class="col-lg-12">
                            <form class="input-wrapper input-wrapper-inline input-wrapper-round">
                                <button class="btn btn-dark btn-close-opup" type="submit">Kapat</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        `;

        var popup_status_false = `
        <div class="newsletter-popup newsletter-pop3" id="${id}">
            <div class="newsletter-content">
                <!-- Popup Title -->
                <h4 class="text-uppercase text-dark"><span class="text-dark">${title}</span></h4>

                <hr class="product-divider">
                
                <!-- Popup Content -->
                <p class="text-grey">
                    ${content}
                </p>
                <div class="col-sm-12">
                    
                    <div class="row" style="margin-bottom:-4rem;">
                        <div class="col-lg-6">
                            <form class="input-wrapper input-wrapper-inline input-wrapper-round">
                                <button class="btn btn-dark btn-close-opup" type="submit">Kapat</button>
                            </form>
                        </div>
                        
                        <div class="col-lg-6">
                            <form action="${formactionurl}" method="post" class="input-wrapper input-wrapper-inline input-wrapper-round">
                                ${csrftoken}
                                <button class="btn ${buttonClass}" type="submit">${buttonName}</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        `;

        if(checkstatuspopup=='True'){
            var popup = popup_status_true
        }else{
            var popup = popup_status_false
        }

        // Open the newsletter popup

        $.magnificPopup.open({
            items: {
                src: popup,
                type: 'inline'
            }
        });
    });

    // Close popup when the close button is clicked
    $('.btn-close-popup').on('click', function (e) {
        e.preventDefault();

        // Close the currently opened popup
        $.magnificPopup.close();
    });
});