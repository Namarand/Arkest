from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Dinosaur
from api.serializers import DinosaurSerializer

@csrf_exempt
def races_list(request):
    if request.method == 'GET':
        dinosaurs = Dinosaur.objects.values('race').distinct()
        races = []
        for i in dinosaurs:
            races += [i['race']]
        return JsonResponse({"count" : len(races), "races" : races}, safe=False)
