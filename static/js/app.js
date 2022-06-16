$(document).ready(function(){

    // $('#id_price, #id_volume, #id_total_price').keyup(function () {
    //     var sale_price = $('#id_price').val();
    //     var sale_volume = $('#id_volume').val();
    //     var sale_total_price = sale_price * sale_volume;

    //     $('#id_total_price').val(sale_total_price);
    // });

    $('#id_price, #id_volume, #id_total_price, #id_amount_paid, #id_balance').keyup(function () {
        var sale_price = $('#id_price').val();        
        // var sale_total_price = $('#id_total_price').val();
        var sale_amount_paid = $('#id_amount_paid').val();
        // var sale_volume = $('#id_volume').val();
        var sale_total_price = $('#id_total_price').val();
        var sale_volume = (sale_total_price/sale_price).toFixed(4);
        var balance = (sale_amount_paid - sale_total_price).toFixed(4);
        
        $('#id_balance').val(balance);
        $('#id_volume').val(sale_volume);
        $('#id_total_price').val(sale_total_price);
    });

    $('#id_price, #id_volume, #id_total_price, #id_amount_paid, #id_balance').click(function () {
        var sale_price = $('#id_price').val();        
        // var sale_total_price = $('#id_total_price').val();
        var sale_amount_paid = $('#id_amount_paid').val();
        // var sale_volume = $('#id_volume').val();
        var sale_total_price = $('#id_total_price').val();
        var sale_volume = (sale_total_price/sale_price).toFixed(4);
        var balance = (sale_amount_paid - sale_total_price).toFixed(4);
        
        $('#id_balance').val(balance);
        $('#id_volume').val(sale_volume);
        $('#id_total_price').val(sale_total_price);
    });

    // $('#id_price, #id_volume, #id_total_price, #amount_paid, #balance').click(function () {
    //     var sale_price = $('#id_price').val();        
    //     var sale_total_price = $('#id_total_price').val();
    //     var amount_paid = $('#id_amount_paid').val();
    //     var sale_volume = (sale_total_price/sale_price).toFixed(4);
    //     var balance = sale_total_price - amount_paid;

    //     $('#id_volume').val(sale_volume);
    //     $('#id_balance').val(balance);
    // });
    
});