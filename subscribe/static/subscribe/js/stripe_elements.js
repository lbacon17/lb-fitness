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
var subscriptionForm = document.getElementById('subscription-form');

subscriptionForm.addEventListener('submit', function (ev) {
    ev.PreventDefault();
    card.update({'disabled': true});
    $('#complete-subscription').attr('disabled', true);

    var saveMemberInfo = Boolean($('#id-save-member-info').attr('checked'));
    var csrfToken = $('input[name=csrfmiddlewaretoken]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_member_info': saveMemberInfo
    };

    var url = '/subscribe/cache_checkout_data/';

    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                member_info: {
                    full_name: $.trim(subscriptionForm.full_name.value),
                    email_address: $.trim(subscriptionForm.email_address.value),
                    phone_number: $.trim(subscriptionForm.phone_number.value),
                },
                billing_info: {
                    cardholder_name: $.trim(subscriptionForm.cardholder_name.value),
                    address: {
                        address_line1: $.trim(subscriptionForm.address_line1.value),
                        address_line2: $.trim(subscriptionForm.address_line2.value),
                        town_or_city: $.trim(subscriptionForm.town_or_city.value),
                        county_or_region: $.trim(subscriptionForm.county_or_region.value),
                        postcode: $.trim(subscriptionForm.postcode.value),
                        country: $.trim(subscriptionForm.country.value)
                    }
                }
            }
        }).then(function(result) {
            if (result.error) {
                var errorElement = document.getElementById('card-errors');
                $(errorElement).html(`<span>${result.error.message}</span>`);
                card.update({'disabled': false});
                $('#complete-subscription').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    subscriptionForm.submit();
                }
            }
        });
    }).fail(function() {
        location.reload();
    })
});