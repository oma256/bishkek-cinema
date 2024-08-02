import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from apps.orders.models import Order
from apps.users.models import User


@csrf_exempt
def order_request(request):
    session_id = int(json.loads(request.body.decode())['session_id'])
    hall_id = int(json.loads(request.body.decode())['hall_id'])
    cinema_id = int(json.loads(request.body.decode())['cinema_id'])
    user = User.objects.filter(id=request.user.id).first()

    for seat in json.loads(request.body.decode())['reserved_seats']:
        row = seat['row']
        place = seat['seat']
        orders = Order.objects.filter(session_id = session_id)

        for order in orders:
            if order.row.id == int(row) and order.place.id == int(place):
                return JsonResponse({'status': 'FAILED'})

        order = Order(user=user,
                      session_id=session_id,
                      hall_id=hall_id,
                      row_id=row,
                      place_id=place,
                      cinema_id=cinema_id)
        order.save()

    return JsonResponse({'status': 'SUCCESS'})
