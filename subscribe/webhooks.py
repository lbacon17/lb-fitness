from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from subscribe.webhook_handler import StripeWH_HandlerSubscribe

import stripe


@require_POST
@csrf_exempt
def webhook(request):
    wh_secret = settings.STRIPE_WH_SECRET2
    stripe.api_key = settings.STRIPE_SECRET_KEY

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        print('one')
        return HttpResponse(content=e, status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print('two')
        return HttpResponse(content=e, status=400)
    except Exception as e:
        print('three')
        return HttpResponse(content=e, status=400)

    handler = StripeWH_HandlerSubscribe(request)

    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    event_type = event['type']

    event_handler = event_map.get(event_type, handler.handle_event)

    response = event_handler(event)

    return response
