// Renders card element on page
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#303238',
        fontSize: '16px',
        fontFamily: '"Open Sans", sans-serif',
        fontSmoothing: 'antialiased',
        '::placeholder': {
        color: '#CFD7DF',
        },
    },
    invalid: {
        color: '#e5424d',
        ':focus': {
        color: '#303238',
        },
    },
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handles real-time validation errors
card.addEventListener('change', function(event) {
    var errorElement = document.getElementById('card-errors');
    if (event.error) {
        $(errorElement).html(`<span>${event.error.message}</span>`);
    } else {
        errorElement.textContent = '';
    }
});

// Handles form submission
var paymentForm = document.getElementById('payment-form');

paymentForm.addEventListener('submit', function (ev) {
    ev.PreventDefault();
    card.update({'disabled': true});
    $('#complete-order').attr('disabled', true);
    $('#payment-form').fadeToggle(100);

    var saveUserInfo = Boolesn($('#id-save-user-info').attr('checked'));
    var csrfToken = $('input[name=csrfmiddlewaretoken]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_user_info': saveUserInfo
    };

    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_info: {
                    full_name: $.trim(paymentForm.full_name.value),
                    email_address: $.trim(paymentForm.email_address.value),
                    phone_number: $.trim(paymentForm.phone_number.value),
                    address: {
                        address_line1: $.trim(paymentForm.address_line1.value),
                        address_line2: $.trim(paymentForm.address_line2.value),
                        town_or_city: $.trim(paymentForm.town_or_city.value),
                        county_or_region: $.trim(paymentForm.county_or_region.value),
                        postcode: $.trim(paymentForm.postcode.value),
                        country: $.trim(paymentForm.country.value)
                    }
                },
                delivery_info: {
                    full_name: $.trim(paymentForm.full_name.value),
                    phone_number: $.trim(paymentForm.phone_number.value),
                    address: {
                        address_line1: $.trim(paymentForm.address_line1.value),
                        address_line2: $.trim(paymentForm.address_line2.value),
                        town_or_city: $.trim(paymentForm.town_or_city.value),
                        county_or_region: $.trim(paymentForm.county_or_region.value),
                        postcode: $.trim(paymentForm.postcode.value),
                        country: $.trim(paymentForm.country.value)
                    }
                }
            }
        }).then(function(result) {
            if (result.error) {
                var errorElement = document.getElementById('card-errors');
                $(errorElement).html(`<span>${result.error.message}</span>`);
                card.update({'disabled': false});
                $('#complete-order').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    paymentForm.submit();
                }
            }
        });
    }).fail(function() {
        location.reload();
    })
});