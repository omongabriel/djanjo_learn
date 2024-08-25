from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("<int:mnt>",views.mnt_int),
    path("<str:mnt>",views.mnt_str,name="mntname")
]