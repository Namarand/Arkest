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

@csrf_exempt
def dinosaurs_list(request, kind):
    if request.method == 'GET':
        dinosaurs = Dinosaur.objects.all().filter(race=kind)
        serializer = DinosaurSerializer(dinosaurs, many=True)
        return JsonResponse({"count" : len(dinosaurs), "dinosaurs": serializer.data}, safe=False)

@csrf_exempt
def dinosaurs(request):
    if request.method == 'GET':
        data = JSONParser().parse(request)
        results = []
        for i in data["ids"]:
            req = Dinosaur.objects.filter(id=i)
            if req.exists():
                results += DinosaurSerializer(req.get()).data
            else:
                results += {"id": i, "error": "no such dinosaurs"}
        return JsonResponse({"dinosaurs": results})
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DinosaurSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def dinosaurs_by_id(request, identifier):
    try:
        dino = Dinosaur.objects.get(pk=identifier)
    except Dinosaur.DoesNotExist:
        return JsonResponse({"id": identifier, "error" : "no sush dinosaurs" }, status=400)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DinosaurSerializer(dino, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        dino.delete()
        return HttpResponse(status=204)

