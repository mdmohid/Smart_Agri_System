from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from .models import ContactMessage

# admin.site.register(User)
admin.site.register(Profile)
admin.site.register(CropRecommendation)
admin.site.register(YieldPrediction)
admin.site.register(MarketPrediction)
admin.site.register(DiseaseDetection)
admin.site.register(ContactMessage)