from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from api.models import Dinosaur
from api.serializers import DinosaurSerializer
from api.permissions import IsApiUser, IsApiViewer

class races_list(APIView):
    permission_classes = (IsApiUser,
                          IsApiViewer)
    def get(self, request):
        dinosaurs = Dinosaur.objects.values('race').distinct()
        races = []
        for i in dinosaurs:
            races += [i['race']]
        return JsonResponse({"count" : len(races), "races" : races}, safe=False)

class dinosaurs_list(APIView):
    permission_classes = (IsApiUser,
                          IsApiViewer)
    def get(self, request, kind):
        dinosaurs = Dinosaur.objects.all().filter(race=kind)
        serializer = DinosaurSerializer(dinosaurs, many=True)
        return JsonResponse({"count" : len(dinosaurs), "dinosaurs": serializer.data}, safe=False)

class dinosaurs(APIView):
    permission_classes = (IsApiUser,
                          IsApiViewer)
    def get(self, request):
        data = JSONParser().parse(request)
        results = []
        for i in data["ids"]:
            req = Dinosaur.objects.filter(id=i)
            if req.exists():
                results += DinosaurSerializer(req.get()).data
            else:
                results += {"id": i, "error": "no such dinosaurs"}
        return JsonResponse({"dinosaurs": results})
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = DinosaurSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class dinosaurs_by_id(APIView):
    permission_classes = (IsApiUser,
                          IsApiViewer)
    def get_by_id(identifier):
        try:
            return Dinosaur.objects.get(pk=identifier)
        except Dinosaur.DoesNotExist:
            raise Http404

    def put(request, identifier):
        dino = get_by_id(identifier)
        data = JSONParser().parse(request)
        serializer = DinosaurSerializer(dino, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, identifier):
        dino = get_by_id(identifier)
        dino.delete()
        return HttpResponse(status=204)

