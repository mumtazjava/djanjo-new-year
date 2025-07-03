from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),         # for http://127.0.0.1:8000/hello/
    path('fahad/', views.fahad ,name="fahad"),   # for http://127.0.0.1:8000/hello/fahad/
    path("faiz/",views.faiz ,name='faiz'),
    path("faisal/",views.faisal,name="faisal"),
    path("<str:name>/",views.greet,name="greet")
]
