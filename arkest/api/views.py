from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Dinosaur
from api.serializers import DinosaurSerializer

@csrf_exempt
def dinosaurs_list(request):
    if request.method == 'GET':
        dinosaurs = Dinosaur.objects.all()
        serializer = DinosaurSerializer(dinosaurs, many=True)
        return JsonResponse(serializer.data, safe=False)
