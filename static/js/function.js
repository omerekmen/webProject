
// Add to cart func.

$('#add-to-cart-button').on('click', function(){
    let product_id = $('#product-id').val();
    let product_title = $('#product-title').val();
    let product_size = $('#product-size .active').text();
    let product_quantity = $('#product-quantity').val();
    let product_price = $('#product-sale-price').val();
    let this_val = $(this);

    console.log('Product Id', product_id);
    console.log('Product Title', product_title);
    console.log('Product Size', product_size);
    console.log('Product Quantity', product_quantity);
    console.log('Product Price', product_price);
    console.log('Active Product', this_val);

    $.ajax({
        url: 'add-to-cart',

    })
    
})