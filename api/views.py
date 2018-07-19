from api.models import Dinosaur
from api.permissions import HasApiRight
from api.serializers import DinosaurSerializer
from rest_framework import permissions
from django.contrib.auth.models import Group, Permission
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

Group.objects.get_or_create(name="ApiUser")
Group.objects.get_or_create(name="ApiViewer")

class races_list(APIView):
    permission_classes = (HasApiRight,)
    def get(self, request):
        dinosaurs = Dinosaur.objects.values('race').distinct()
        races = []
        for i in dinosaurs:
            races += [i['race']]
        return JsonResponse({"count" : len(races), "races" : races}, safe=False)

class dinosaurs_list(APIView):
    permission_classes = (HasApiRight,)
    def get(self, request, kind):
        dinosaurs = Dinosaur.objects.all().filter(race=kind)
        if len(dinosaurs) == 0:
            raise Http404
        serializer = DinosaurSerializer(dinosaurs, many=True)
        return JsonResponse({"count" : len(dinosaurs), "dinosaurs": serializer.data}, safe=False)

class dinosaurs(APIView):
    permission_classes = (HasApiRight,)
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = DinosaurSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class dinosaurs_by_id(APIView):
    permission_classes = (HasApiRight,)
    def get_by_id(self, identifier):
        try:
            return Dinosaur.objects.get(pk=identifier)
        except Dinosaur.DoesNotExist:
            raise Http404

    def get(self, request, identifier):
        return JsonResponse(DinosaurSerializer(self.get_by_id(identifier)).data)

    def put(self, request, identifier):
        dino = self.get_by_id(identifier)
        data = JSONParser().parse(request)
        serializer = DinosaurSerializer(dino, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, identifier):
        dino = self.get_by_id(identifier)
        dino.delete()
        return HttpResponse(status=204)

