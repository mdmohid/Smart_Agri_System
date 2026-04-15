
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

    path('logout/', views.logout_view, name='logout'),

    #farmer dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    path('verify-otp/', views.verify_otp, name='verify_otp'),

    path('dashboard/history/<str:type>/', views.history_view, name='history'),

    # path('reset-password/', views.password_reset_confirm, name='password_reset_confirm'),
    # path('reset-password/<str:uidb64>/<str:token>/', views.password_reset_confirm, name='password_reset_confirm_link'),
    path('password-reset-request/', views.password_reset_request, name='password_reset_request'),
    path('reset-password/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset-password/<str:uidb64>/<str:token>/', views.password_reset_confirm, name='password_reset_confirm_link'),

    path('send-reset-code/', views.send_reset_code, name='send_reset_code'),
    path('verify-reset-code/', views.verify_reset_code, name='verify_reset_code'),
]