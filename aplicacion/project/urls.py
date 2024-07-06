from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('deportes/', views.deportes, name="deportes"),
    path('Deportes.html', views.deportes,),
    path('quienessomos.html', views.quienessomos,name="quienessomos"),
    path('instalaciones.html', views.instalaciones,name="instalaciones"),

]
