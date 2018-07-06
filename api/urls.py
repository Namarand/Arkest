from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^dinosaurs/list/$', views.races_list.as_view()),
    url(r'^dinosaurs/list/(?P<kind>[a-zA-Z]+)/$', views.dinosaurs_list.as_view()),
    url(r'^dinosaurs/$', views.dinosaurs.as_view()),
    url(r'^dinosaurs/(?P<identifier>[0-9]+)/$', views.dinosaurs_by_id.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
