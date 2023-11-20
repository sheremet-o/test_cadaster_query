from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators import csrf_exempt

from .models import CadasterRequest


@csrf_exempt
def result(request):
    if request.method == 'POST':
        data = request.POST
        result = data.get('result') # noqa

        return JsonResponse({'message': 'Получен результат'})


def ping(request):
    return JsonResponse({'message': 'Сервер запустился'})


def history(request):
    cadaster_number = request.GET.get('cadaster_number')

    query = CadasterRequest.objects.filter(
        cadaster_number=cadaster_number)
    result = [{'cadaster_number': item.cadaster_number,
               'latitude': item.latitude,
               'longitude': item.longitude,
               'result': item.result,
               'timestamp': item.timestamp} for item in query]
    return JsonResponse({'history': result})
