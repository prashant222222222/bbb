from django.conf.urls import url
from . import views

app_name='os1'

urlpatterns = [
    url(r'^help/$',views.help,name='help'),
    url(r'^index/$',views.index,name='index'),
]
