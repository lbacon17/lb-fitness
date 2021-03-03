// Logic, templating and CSS recommendations taken from Stripe documentation:
// https://stripe.com/docs/payments/accept-a-payment
// https://stripe.com/docs/stripe-js

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