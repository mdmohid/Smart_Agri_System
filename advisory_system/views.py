# # Create views here.
# # crop recommendation views

# from django.shortcuts import render
# from .forms import CropForm
# from ml_models.crop_recommendation.predictor import predict_crop
# #from .models import CropPrediction  # optional if you want DB storage

# def crop_recommendation_view(request):
#     recommended_crop = None
#     if request.method == "POST":
#         form = CropForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             recommended_crop = predict_crop(
#                 data['N'], data['P'], data['K'],
#                 data['temperature'], data['humidity'],
#                 data['ph'], data['rainfall']
#             )

#             # Optional: Save to DB
#             # CropPrediction.objects.create(**data, predicted_crop=recommended_crop)
#     else:
#         form = CropForm()

#     return render(request, "crop_form.html", {
#         "form": form,
#         "recommended_crop": recommended_crop
#     })


# #from django.shortcuts import render

# def index(request):
#     return render(request, 'index.html')



# your_app/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def features(request):
    return render(request, 'features.html')

def contact(request):
    return render(request, 'contact.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')