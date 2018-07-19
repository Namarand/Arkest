from parents.models import Parents
from api.permissions import HasApiRight
from parents.serializers import ParentsSerializer
from rest_framework import permissions
from django.contrib.auth.models import Group, Permission
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

class parents(APIView):
    permission_classes = (HasApiRight,)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ParentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class parents_by_id(APIView):
    permission_classes = (HasApiRight,)

    def get_by_id(self, identifier):
        try:
            return Parents.objects.get(pk=identifier)
        except Dinosaur.DoesNotExist:
            raise Http404

    def get(self, request, identifier):
        return JsonResponse(ParentsSerializer(self.get_by_id(identifier)).data)

    def put(self, request, identifier):
        parents = self.get_by_id(identifier)
        data = JSONParser().parse(request)
        serializer = DinosaurSerializer(parents, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, identifier):
        parents = self.get_by_id(identifier)
        parents.delete()
        return HttpResponse(status=204)
