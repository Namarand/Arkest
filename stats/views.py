from stats.models import RaceStats
from stats.serializers import *
from rest_framework import permissions
from django.contrib.auth.models import Group, Permission
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

class race_stats_creator(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = RaceStatsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class race_stats_accessor(APIView):
    def get_by_id(self, identifier):
        try:
            return RaceStats.objects.get(pk=identifier)
        except RaceStats.DoesNotExist:
            raise Http404

    def get(self, request, race):
        return JsonResponse(RaceStatsSerializer(self.get_by_id(identifier)).data)

    def put(self, request, race):
        stats = self.get_by_id(identifier)
        data = JSONParser().parse(request)
        serializer = RaceStatsSerializer(stats, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, race):
        self.get_by_id(identifier).delete()
        return HttpResponse(status=204)
