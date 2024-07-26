import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from apps.orders.models import Order


@csrf_exempt
def order_request(request):
    session_id = int(json.loads(request.body.decode())['session_id'])
    hall_id = int(json.loads(request.body.decode())['hall_id'])

    for seat in json.loads(request.body.decode())['reserved_seats']:
        row = seat['row']
        place = seat['seat']

        order = Order(user=request.user.id,
                      session_id=session_id,
                      hall_id=hall_id,
                      row_id=row,
                      place_id=place)
        order.save()

    return JsonResponse({'status': 'SUCCESS'})
