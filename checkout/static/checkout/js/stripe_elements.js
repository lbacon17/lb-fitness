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
        var html = `
            <span class="text-danger"><i class="fas fa-exclamation-circle"></i> ${event.error.message}</span>`;
        $(errorElement).html(html);
    } else {
        errorElement.textContent = '';
    }
});

// Handles form submission
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({'disabled': true});
    $('#complete-order').attr('disabled', true);
    $('#payment-form').fadeToggle(100);

    var saveUserInfo = Boolean($('#id-save-user-info').attr('checked'));
    var csrfToken = $('input[name=csrfmiddlewaretoken]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_user_info': saveUserInfo,
    };

    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email_address.value),
                    address: {
                        line1: $.trim(form.address_line1.value),
                        line2: $.trim(form.address_line2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county_or_region.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.address_line1.value),
                    line2: $.trim(form.address_line2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county_or_region.value),
                }
            },
        }).then(function(result) {
            if (result.error) {
                var errorElement = document.getElementById('card-errors');
                var html = `
                    <span class="text-danger"><i class="fas fa-exclamation-circle"></i> ${event.error.message}</span>`;
                $(errorElement).html(html);
                card.update({'disabled': false});
                $('#complete-order').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function() {
        location.reload();
    })
});