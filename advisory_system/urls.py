
#crop recommendation url routing
from django.urls import path
from . import views

from .views import crop_recommendation_view

urlpatterns = [
  path('', views.index, name='home'),
  path('crop/', crop_recommendation_view, name='crop_recommendation'),
]