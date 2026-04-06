from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(CropRecommendation)
admin.site.register(YieldPrediction)
admin.site.register(MarketPrediction)
admin.site.register(DiseaseDetection)