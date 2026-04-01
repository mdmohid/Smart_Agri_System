

# # Create models here.
# #crop recommendation model


# from django.db import models

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