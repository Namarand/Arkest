from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^dinosaurs/list$', views.races_list),
]
