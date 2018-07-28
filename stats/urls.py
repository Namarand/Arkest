from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework.urlpatterns import format_suffix_patterns
from stats import views

urlpatterns = [
    url(r'^stats/$', views.category_list.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
