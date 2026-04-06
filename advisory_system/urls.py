
# #crop recommendation url routing
# from django.urls import path
# from . import views

# from .views import crop_recommendation_view

# urlpatterns = [
#   path('', views.index, name='home'),
#   path('crop/', crop_recommendation_view, name='crop_recommendation'),
# ]



# your_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('features/', views.features, name='features'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]