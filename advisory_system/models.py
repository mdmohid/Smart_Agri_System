
# # Create models here.
# #crop recommendation model


#from django.db import models

# class CropPrediction(models.Model):
#     N = models.FloatField()
#     P = models.FloatField()
#     K = models.FloatField()
#     temperature = models.FloatField()
#     humidity = models.FloatField()
#     ph = models.FloatField()
#     rainfall = models.FloatField()
#     predicted_crop = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.predicted_crop} at {self.created_at}"



# All the Models are here 
from django.db import models

#user Model
class User(models.Model):
    ROLE_CHOICES = (
        ('farmer', 'Farmer'),
        ('admin', 'Admin'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='farmer')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


#crop recommendation model
class CropRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField()
    rainfall = models.FloatField()

    recommended_crop = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Crop - {self.recommended_crop}"
    

#yield prediction model
class YieldPrediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    area = models.FloatField()
    crop = models.CharField(max_length=100)
    year = models.IntegerField()
    average_rainfall = models.FloatField()
    pesticides_tonnes = models.FloatField()
    avg_temp = models.FloatField()

    predicted_yield = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Yield - {self.crop}"
    

#market prediction model
class MarketPrediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    year = models.IntegerField()
    month = models.IntegerField()
    crop = models.CharField(max_length=100)
    market = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    predicted_price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Market - {self.crop}"
    

#disease detection
class DiseaseDetection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='disease_images/')
    disease_name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.disease_name