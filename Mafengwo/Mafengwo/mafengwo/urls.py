from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^echarts/(?P<city>\w+)/$', views.Mafengwo.as_view()),
    url(r'^', views.index),

]