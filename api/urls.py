from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^dinosaurs/$', views.dinosaurs_list),
]
