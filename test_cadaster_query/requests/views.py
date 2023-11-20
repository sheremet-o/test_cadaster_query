import time

from django.http import JsonResponse

from .models import CadasterRequest


def query(request):
    if request.method == 'POST':
        data = request.POST
        cadaster_number = data.get('cadaster_number')
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        time.sleep

        result = True

        request_data = CadasterRequest(
            cadaster_number=cadaster_number,
            latitude=latitude,
            longitude=longitude,
            result=result
        )
        request_data.save()

        return JsonResponse({'result': result})


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
