from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework.urlpatterns import format_suffix_patterns
from parents import views

urlpatterns = [
    url(r'^parents/$', views.parents.as_view()),
    url(r'^parents/(?P<identifier>[0-9]+)/$', views.parents_by_id.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
