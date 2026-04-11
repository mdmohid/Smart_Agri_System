# # # Create views here.
# # # crop recommendation views

# # from django.shortcuts import render
# # from .forms import CropForm
# # from ml_models.crop_recommendation.predictor import predict_crop
# # #from .models import CropPrediction  # optional if you want DB storage

# # def crop_recommendation_view(request):
# #     recommended_crop = None
# #     if request.method == "POST":
# #         form = CropForm(request.POST)
# #         if form.is_valid():
# #             data = form.cleaned_data
# #             recommended_crop = predict_crop(
# #                 data['N'], data['P'], data['K'],
# #                 data['temperature'], data['humidity'],
# #                 data['ph'], data['rainfall']
# #             )

# #             # Optional: Save to DB
# #             # CropPrediction.objects.create(**data, predicted_crop=recommended_crop)
# #     else:
# #         form = CropForm()

# #     return render(request, "crop_form.html", {
# #         "form": form,
# #         "recommended_crop": recommended_crop
# #     })


# # #from django.shortcuts import render

# # def index(request):
# #     return render(request, 'index.html')



# # your_app/views.py
# from django.shortcuts import render

# def home(request):
#     return render(request, 'index.html')

# def about(request):
#     return render(request, 'about.html')

# def features(request):
#     return render(request, 'features.html')

# def contact(request):
#     return render(request, 'contact.html')

# # def login_view(request):
# #     return render(request, 'login.html')

# # def register_view(request):
# #     return render(request, 'register.html')


# #register view 
# from django.shortcuts import render, redirect
# from .models import User

# def register_view(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         User.objects.create(
#             name=name,
#             email=email,
#             password=password,
#             role='farmer'
#         )

#         return redirect('dashboard')   # IMPORTANT

#     return redirect('home')  # no direct page



# #login view
# # def login_view(request):
# #     if request.method == "POST":
# #         email = request.POST.get('email')
# #         password = request.POST.get('password')

# #         try:
# #             user = User.objects.get(email=email, password=password)

# #             request.session['user_id'] = user.id

# #             return redirect('dashboard')   #IMPORTANT

# #         except:
# #             return redirect('home')

# #     return redirect('home')



# #farmer dashboard
# # def dashboard(request):
# #     return render(request, 'dashboard.html')

# def dashboard(request):
#     if 'user_id' not in request.session:
#         return redirect('home')

#     return render(request, 'dashboard.html')




# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from .models import CropRecommendation, YieldPrediction, DiseaseDetection, MarketPrediction

# # HOME
# def home(request):
#     return render(request, 'index.html')


# # LOGIN
# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get('email')   # using email as username
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('dashboard')
#         else:
#             return redirect('home')

#     return redirect('home')


# # LOGOUT
# def logout_view(request):
#     logout(request)
#     return redirect('home')


# # DASHBOARD
# @login_required
# def dashboard(request):
#     user = request.user

#     crop_count = CropRecommendation.objects.filter(user=user).count()
#     yield_count = YieldPrediction.objects.filter(user=user).count()
#     disease_count = DiseaseDetection.objects.filter(user=user).count()

#     context = {
#         'crop_count': crop_count,
#         'yield_count': yield_count,
#         'disease_count': disease_count,
#     }

#     return render(request, 'dashboard.html', context)






from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import CropRecommendation, YieldPrediction, DiseaseDetection, MarketPrediction


# Home
def home(request):
    return render(request, 'index.html')

#About us
def about(request):
    return render(request, 'about.html')

#Features
def features(request):
    return render(request, 'features.html')

#contact us
def contact(request):
    return render(request, 'contact.html')


# REGISTER (FIXED)
# def register_view(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # create user
#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password
#         )

#         # login automatically
#         login(request, user)

#         return redirect('dashboard')

#     return redirect('home')




# def register_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         confirm_password = request.POST.get("confirm_password")

#         if password != confirm_password:
#             messages.error(request, "Passwords do not match!")
#             return redirect("register")

#         # Check if username already exists
#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already taken!")
#             return redirect("register")

#         # Create user if valid
#         user = User.objects.create_user(username=username, email=email, password=password)
#         user.save()
#         messages.success(request, "Account created successfully!")
#         return redirect("login")

#     return render(request, "register.html")



def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("register")

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Log the user in automatically
        login(request, user)

        messages.success(request, "Account created successfully!")
        return redirect("dashboard")  # <-- go to dashboard after registration

    return redirect('home')



# LOGIN (FIXED)
def login_view(request):
    if request.method == "POST":
        #email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')

    return redirect('home')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('home')


# # FARMER DASHBOARD (FIXED)
# @login_required
# def dashboard(request):
#     user = request.user

#     crop_count = CropRecommendation.objects.filter(user=user).count()
#     yield_count = YieldPrediction.objects.filter(user=user).count()
#     disease_count = DiseaseDetection.objects.filter(user=user).count()
#     market_count = MarketPrediction.objects.filter(user=user).count()

#     context = {
#         'crop_count': crop_count,
#         'yield_count': yield_count,
#         'disease_count': disease_count,
#         'market_count' : market_count
#     }

#     return render(request, 'dashboard.html', context)




from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import CropRecommendation, YieldPrediction, DiseaseDetection, MarketPrediction

# importing all ML models
from ml_models.crop_recommendation.predictor import predict_crop
from ml_models.yield_prediction.predictor import predict_yield
from ml_models.disease_detection.predictor import predict_disease

@login_required
def dashboard(request):
    crop_result = None  
    yield_result = None
    disease_result = None
    active_modal = None

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        #  Crop Recommendation
        if form_type == "crop":
            nitrogen = float(request.POST.get('nitrogen'))
            phosphorus = float(request.POST.get('phosphorus'))
            potassium = float(request.POST.get('potassium'))
            temperature = float(request.POST.get('temperature'))
            humidity = float(request.POST.get('humidity'))
            ph = float(request.POST.get('ph'))
            rainfall = float(request.POST.get('rainfall'))

            #  ML Prediction
            crop_result = predict_crop(
                nitrogen, phosphorus, potassium,
                temperature, humidity, ph, rainfall
            )

            # Saving to DB
            CropRecommendation.objects.create(
                user=request.user,
                nitrogen=nitrogen,
                phosphorus=phosphorus,
                potassium=potassium,
                temperature=temperature,
                humidity=humidity,
                ph=ph,
                rainfall=rainfall,
                recommended_crop=crop_result
            )

            active_modal = "crop"    

        # yield prediction
        elif form_type == "yield":
            area = request.POST.get('area')
            crop = request.POST.get('crop')
            year = int(request.POST.get('year'))
            rainfall = float(request.POST.get('average_rainfall'))
            pesticides = float(request.POST.get('pesticides_tonnes'))
            temperature = float(request.POST.get('avg_temp'))
        
            # ML PREDICTION
            yield_result = predict_yield(
                area, crop, year, rainfall, pesticides, temperature
            )
        
            # SAVE TO DB
            YieldPrediction.objects.create(
                user=request.user,
                area=area,
                crop=crop,
                year=year,
                average_rainfall=rainfall,
                pesticides_tonnes=pesticides,
                avg_temp=temperature,
                predicted_yield=yield_result
            )
        
            active_modal = "yield"


        elif form_type == "disease":
        
            uploaded_image = request.FILES.get("image")
        
            from django.core.files.storage import FileSystemStorage
            fs = FileSystemStorage()
            filename = fs.save(uploaded_image.name, uploaded_image)
            file_path = fs.path(filename)
        
            # ML CALL
            disease_result = predict_disease(file_path)
        
            # Save DB
            DiseaseDetection.objects.create(
                user=request.user,
                image=filename,
                disease_name=disease_result
            )
        
            active_modal = "disease"





    # stats
    context = {
        'crop_result': crop_result,
        'yield_result': yield_result,
        'disease_result': disease_result,
        'active_modal': active_modal,
        'crop_count': CropRecommendation.objects.filter(user=request.user).count(),
        'yield_count': YieldPrediction.objects.filter(user=request.user).count(),
        'disease_count': DiseaseDetection.objects.filter(user=request.user).count(),
        'market_count': MarketPrediction.objects.filter(user=request.user).count(),
    }

    return render(request, 'dashboard.html', context)