from django.urls import path
from . import views
# URLConf
urlpatterns = [ # Precisa ser esse o nome
  path(‘primeiroapp/oi’, views.diga_oi)
]