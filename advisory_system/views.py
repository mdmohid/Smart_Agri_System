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
# def contact(request):
#     return render(request, 'contact.html')

from .models import ContactMessage
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to DB
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        messages.success(request, "Message sent successfully!")
        return redirect('contact')

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



# def register_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         confirm_password = request.POST.get("confirm_password")

#         # Check if passwords match
#         if password != confirm_password:
#             messages.error(request, "Passwords do not match!")
#             return redirect("register")

#         # Check if username already exists
#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already taken!")
#             return redirect("register")

#         # Create the user
#         user = User.objects.create_user(username=username, email=email, password=password)
#         user.save()

#         # Log the user in automatically
#         login(request, user)

#         messages.success(request, "Account created successfully!")
#         return redirect("dashboard")  # <-- go to dashboard after registration

#     return redirect('home')


from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail

from .utils import generate_otp
from django.conf import settings
from .models import Profile



# def register_view(request):
#     if request.method == "POST":

#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         confirm_password = request.POST.get("confirm_password")

#         #  validations
#         if password != confirm_password:
#             messages.error(request, "Passwords do not match!")
#             return redirect("register")

#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already taken!")
#             return redirect("register")

#         #  create user (inactive)
#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password
#         )
#         user.is_active = False
#         user.save()

#         #  generate OTP
#         otp = generate_otp()

#         #  save OTP in profile
#         # profile = user.profile
#         profile, _ = Profile.objects.get_or_create(user=user)
#         profile.otp = otp
#         profile.save()

#         #  send email
#         # send_mail(
#         #     "Your OTP Code",
#         #     f"Your OTP is: {otp}",
#         #     "your_email@gmail.com",
#         #     [email],
#         # )
        
#         send_mail(
#             "Your OTP Code for Registering of AgriSmart",
#             f"Your OTP is: {otp}",
#             settings.EMAIL_HOST_USER,   # correct
#             [email],
#             fail_silently=False,
#         )

#         # store user in session
#         request.session['user_id'] = user.id

#         messages.success(request, "OTP sent to your email")
#         return redirect('verify_otp')

#     return redirect('home')

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail

from .utils import generate_otp
from django.conf import settings
from .models import Profile
from django.db import connection
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Validations
        if password != confirm_password:
            request.session['register_error'] = "Passwords do not match!"
            return redirect('home')

        if User.objects.filter(username=username).exists():
            request.session['register_error'] = "Username already taken!"
            return redirect('home')

        # Create user (inactive)
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_active = False
        user.save()

        # Generate OTP
        otp = generate_otp()
        profile, _ = Profile.objects.get_or_create(user=user)
        profile.otp = otp
        # profile.save()
        profile.save(update_fields=['otp'])  # force update

        
        
        # profile, _ = Profile.objects.get_or_create(user=user)
        # # Direct SQL update – bypasses transaction rollback
        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         "UPDATE advisory_system_profile SET otp = %s WHERE user_id = %s",
        #         [otp, user.id]
        #     )

        # Send email
        send_mail(
            "Your OTP Code for Registering of AgriSmart",
            f"Your OTP is: {otp}",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        # Store user ID and flag to open OTP modal
        request.session['user_id'] = user.id
        request.session['show_otp_modal'] = True
        request.session['otp_success'] = "OTP sent to your email"

        return redirect('home')

    return redirect('home')



# OTP view
# from django.contrib.auth import login

# def verify_otp(request):
#     if request.method == "POST":
#         otp_input = request.POST.get("otp")

#         user_id = request.session.get('user_id')
#         user = User.objects.get(id=user_id)

#         if user.profile.otp == otp_input:

#             user.profile.is_verified = True
#             user.profile.otp = None
#             user.profile.save()

#             user.is_active = True
#             user.save()

#             login(request, user)

#             return redirect('dashboard')

#         else:
#             messages.error(request, "Invalid OTP")

#     return render(request, "verify_otp.html")



def verify_otp(request):
    if request.method == "POST":
        otp_input = request.POST.get("otp")
        user_id = request.session.get('user_id')

        if not user_id:
            request.session['otp_error'] = "Session expired. Please register again."
            return redirect('home')

        user = User.objects.get(id=user_id)

        if user.profile.otp == otp_input:
            # OTP correct
            user.profile.is_verified = True
            user.profile.otp = None
            user.profile.save()
            user.is_active = True
            user.save()
            login(request, user)
            # Clear OTP flag and user_id
            request.session.pop('show_otp_modal', None)
            request.session.pop('user_id', None)
            return redirect('dashboard')
        else:
            # Wrong OTP – reopen modal with error
            request.session['show_otp_modal'] = True
            request.session['otp_error'] = "Invalid OTP. Please try again."
            return redirect('home')

    return redirect('home')




# # LOGIN (FIXED)
# def login_view(request):
#     if request.method == "POST":
#         #email = request.POST.get('email')
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user:
#             login(request, user)
#             return redirect('dashboard')

#     return redirect('home')


# def login_view(request):
#     if request.method == "POST":

#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user:

#             # Block unverified users
#             if not user.profile.is_verified:
#                 messages.error(request, "Please verify OTP first")
#                 return redirect('login')

#             login(request, user)

#             # Admin vs Farmer
#             if user.is_superuser:
#                 return redirect('/admin/')

#             return redirect('dashboard')

#     return redirect('home')

# def login_view(request):
#     if request.method == "POST":

#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user:

#             # ADMIN: skip OTP check
#             if user.is_superuser:
#                 login(request, user)
#                 return redirect('/admin/')

#             # Farmer must verify OTP
#             if not user.profile.is_verified:
#                 messages.error(request, "Verify OTP first")
#                 return redirect('login')

#             login(request, user)
#             return redirect('dashboard')

#     return redirect('home')


# def login_view(request):
#     if request.method == "POST":

#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user:

#             # BLOCK ADMIN FROM MODAL LOGIN
#             if user.is_superuser or user.is_staff:
#                 messages.error(request, "Admin must login through admin panel only")
#                 return redirect('/admin/')

#             # Farmer OTP check
#             if not user.profile.is_verified:
#                 messages.error(request, "Verify OTP first")
#                 return redirect('home')

#             login(request, user)
#             return redirect('dashboard')

#     return redirect('home')

# def login_view(request):
#     if request.method == "POST":

#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user:

#             # ADMIN ONLY via /admin/
#             if user.is_superuser:
#                 messages.error(request, "Use /admin/ for admin login")
#                 return redirect('/admin/login/')

#             # FARMER ONLY
#             if not user.profile.is_verified:
#                 messages.error(request, "Verify OTP first")
#                 return redirect('login')

#             login(request, user)
#             return redirect('dashboard')

#     return redirect('home')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            if user.is_superuser:
                request.session['login_error'] = "Use /admin/ for admin login"
                return redirect('/admin/login/')
            if not user.profile.is_verified:
                request.session['login_error'] = "Please verify OTP first"
                return redirect('home')
            login(request, user)
            return redirect('dashboard')
        else:
            request.session['login_error'] = "Invalid username or password"
            return redirect('home')
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
from django.shortcuts import render, redirect

# importing all ML models
from ml_models.crop_recommendation.predictor import predict_crop
from ml_models.yield_prediction.predictor import predict_yield
from ml_models.disease_detection.predictor import predict_disease
from ml_models.market_prediction.predictor import predict_price

@login_required
def dashboard(request):
    
    # BLOCK ADMIN HERE
    # if request.user.is_superuser:
    #   return redirect('/admin/')   # or show error
    # if request.user.is_superuser:
            
    #         print("ADMIN BLOCKED")  # DEBUG LINE
    #         return redirect('/admin/')
    
    # print("FARMER ACCESS")  # DEBUG LINE

    # ONLY FARMER ALLOWED
    if request.user.is_superuser:
            return redirect('/admin/')   # or 403 page
    
    crop_error = None
    yield_error = None
    disease_error = None
    market_error = None
    crop_result = None  
    yield_result = None
    disease_result = None
    market_result = None
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
            # crop_result = predict_crop(
            #     nitrogen, phosphorus, potassium,
            #     temperature, humidity, ph, rainfall
            # )

            try:
                crop_result = predict_crop(
                    nitrogen, phosphorus, potassium,
                    temperature, humidity, ph, rainfall
                )
            except ValueError as e:
                crop_result = "Uncertain (input out of range)"
                crop_error= f"Crop recommendation could not be determined: {str(e)}"

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
        
            # # ML PREDICTION
            # yield_result = predict_yield(
            #     area, crop, year, rainfall, pesticides, temperature
            # )

            try:
                yield_result = predict_yield(
                    area, crop, year, rainfall, pesticides, temperature
                )
            except ValueError as e:
                if "unseen labels" in str(e):
                    yield_result = 0.0
                    yield_error=f"Unknown crop : '{crop}'. Please use supported values."
                else:
                    yield_result = 0.0
                    yield_error= f"Yield prediction failed: {str(e)}"
            except Exception as e:
                yield_result = 0.0
                yield_error= f"Yield prediction error: {str(e)}"
        
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


        #disease detection
        elif form_type == "disease":
        
            uploaded_image = request.FILES.get("image")
        
            from django.core.files.storage import FileSystemStorage
            fs = FileSystemStorage()
            filename = fs.save(uploaded_image.name, uploaded_image)
            file_path = fs.path(filename)
        
            # ML CALL
            # disease_result = predict_disease(file_path)
            try:
                disease_result = predict_disease(file_path)
            except Exception as e:
                disease_result = "Detection failed"
                disease_error=f"Disease detection error: {str(e)}"
        
            # Save DB
            DiseaseDetection.objects.create(
                user=request.user,
                image=filename,
                disease_name=disease_result
            )
        
            active_modal = "disease"

        #market price prediction
        elif form_type == "market":
            year = int(request.POST.get("year"))
            month = int(request.POST.get("month"))
            crop = request.POST.get("crop")
            market = request.POST.get("market")
            country = request.POST.get("country")
        
            #ML prediction
            # market_result = predict_price(year, month, crop, market, country)
            try:
                market_result = predict_price(year, month, crop, market, country)
            except ValueError as e:
                if "unseen labels" in str(e):
                    market_result = 0.0
                    market_error=f"Unknown crop: '{crop}'. Please use supported values."
                else:
                    market_result = 0.0
                    market_error=f"Market prediction failed: {str(e)}"
            except Exception as e:
                market_result = 0.0
                market_error= f"Market prediction error: {str(e)}"
        

            #save to DB
            MarketPrediction.objects.create(
                user=request.user,
                year=year,
                month=month,
                crop=crop,
                market=market,
                country=country,
                predicted_price=market_result
            )
        
            active_modal = "market"




    # stats
    context = {
        
        'crop_error': crop_error,
        'yield_error': yield_error,
        'disease_error': disease_error,
        'market_error': market_error,

        'crop_result': crop_result,
        'yield_result': yield_result,
        'disease_result': disease_result,
        'market_result': market_result,
        'active_modal': active_modal,
        'crop_count': CropRecommendation.objects.filter(user=request.user).count(),
        'yield_count': YieldPrediction.objects.filter(user=request.user).count(),
        'disease_count': DiseaseDetection.objects.filter(user=request.user).count(),
        'market_count': MarketPrediction.objects.filter(user=request.user).count(),
        
    }

    return render(request, 'dashboard.html', context)



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CropRecommendation, YieldPrediction, DiseaseDetection, MarketPrediction

@login_required
def history_view(request, type):
    user = request.user
    if type == 'crop':
        records = CropRecommendation.objects.filter(user=user).order_by('-created_at')
        context = {'records': records, 'type': 'crop'}
        return render(request, 'dashboard_history_crop.html', context)
    elif type == 'yield':
        records = YieldPrediction.objects.filter(user=user).order_by('-created_at')
        context = {'records': records, 'type': 'yield'}
        return render(request, 'dashboard_history_yield.html', context)
    elif type == 'disease':
        records = DiseaseDetection.objects.filter(user=user).order_by('-created_at')
        context = {'records': records, 'type': 'disease'}
        return render(request, 'dashboard_history_disease.html', context)
    elif type == 'market':
        records = MarketPrediction.objects.filter(user=user).order_by('-created_at')
        context = {'records': records, 'type': 'market'}
        return render(request, 'dashboard_history_market.html', context)
    else:
        return render(request, 'dashboard_history_error.html')
    


def home(request):
    # Pop session flags and messages
    show_otp_modal = request.session.pop('show_otp_modal', False)
    otp_success = request.session.pop('otp_success', None)
    otp_error = request.session.pop('otp_error', None)
    login_error = request.session.pop('login_error', None)
    register_error = request.session.pop('register_error', None)

    reset_step = request.session.pop('reset_step', None)
    reset_success = request.session.pop('reset_success', None)
    reset_error = request.session.pop('reset_error', None)

    open_login_modal = request.session.pop('open_login_modal', False)



    context = {
        'show_otp_modal': show_otp_modal,
        'otp_success': otp_success,
        'otp_error': otp_error,
        'login_error': login_error,
        'register_error': register_error,

        'reset_step': reset_step,
        'reset_success': reset_success,
        'reset_error': reset_error,

        'open_login_modal': open_login_modal,
    }
    return render(request, 'index.html', context)



from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import redirect, render

def password_reset_confirm(request, uidb64, token):
    if request.method == "POST":
        uidb64 = request.POST.get('uidb64')
        token = request.POST.get('token')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            request.session['reset_error'] = "Passwords do not match."
            return redirect('home')
        
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, User.DoesNotExist):
            user = None
        
        if user and default_token_generator.check_token(user, token):
            user.set_password(password)
            user.save()
            request.session['reset_success'] = "Password changed successfully. Please login."
            return redirect('home')
        else:
            request.session['reset_error'] = "Invalid or expired reset link."
            return redirect('home')
    
    # GET request – redirect to home with query parameters
    return redirect(f'/?uidb64={uidb64}&token={token}')


from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings

def password_reset_request(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            # user = User.objects.get(email=email)
            user = User.objects.filter(email=email).first()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = request.build_absolute_uri(f'/reset-password/{uid}/{token}/')
            send_mail(
                "Reset your password - AgriSmart",
                f"Click the link to reset your password: {reset_link}",
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            request.session['reset_success'] = "Reset link sent to your email."
        except User.DoesNotExist:
            request.session['reset_error'] = "No account with that email."
        return redirect('home')
    return redirect('home')


import random
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.conf import settings

# def send_reset_code(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         username = request.POST.get("username")
#         try:
#             # user = User.objects.get(email=email)
#             # user = User.objects.filter(email=email).first()
#             user = User.objects.get(email=email, username=username)
#             code = str(random.randint(100000, 999999))
#             request.session['reset_code'] = code
#             request.session['reset_email'] = email
#             send_mail(
#                 "Your password reset code",
#                 f"Your code is: {code}",
#                 settings.DEFAULT_FROM_EMAIL,
#                 [email],
#                 fail_silently=False,
#             )
#             request.session['reset_step'] = 2
#         except User.DoesNotExist:
#             request.session['reset_error'] = "No account with that email and username."
#         return redirect('home')
#     return redirect('home')

# def verify_reset_code(request):
#     if request.method == "POST":
#         code = request.POST.get("code")
#         password = request.POST.get("password")
#         confirm = request.POST.get("confirm_password")
#         if password != confirm:
#             request.session['reset_error'] = "Passwords do not match"
#         elif code != request.session.get('reset_code'):
#             request.session['reset_error'] = "Invalid code"
#         else:
#             email = request.session.get('reset_email')
            
#             # user = User.objects.get(email=email)
#             user = User.objects.filter(email=email).first()
#             user.set_password(password)
#             user.save()
#             # request.session['reset_success'] = "Password changed. Please login."
#             request.session['reset_success'] = f"Password changed. Please login with username: {user.username}"
#             request.session['open_login_modal'] = True
#             request.session.pop('reset_code', None)
#             request.session.pop('reset_email', None)
#             request.session.pop('reset_step', None)
#         return redirect('home')
#     return redirect('home')

# def verify_reset_code(request):
#     if request.method == "POST":
#         code = request.POST.get("code")
#         password = request.POST.get("password")
#         confirm = request.POST.get("confirm_password")
#         if password != confirm:
#             request.session['reset_error'] = "Passwords do not match"
#         elif code != request.session.get('reset_code'):
#             request.session['reset_error'] = "Invalid code"
#         else:
#             email = request.session.get('reset_email')
#             username = request.session.get('reset_username')
          
#             user = User.objects.get(email=email, username=username)
#             user.set_password(password)
#             user.save()
#             request.session['reset_success'] = f"Password changed for user '{username}'. Please login."
#             request.session['open_login_modal'] = True
#             request.session.pop('reset_code', None)
#             request.session.pop('reset_email', None)
#             request.session.pop('reset_username', None)
#             request.session.pop('reset_step', None)
            
#         return redirect('home')
#     return redirect('home')


def verify_reset_code(request):
    if request.method == "POST":
        code = request.POST.get("code")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm_password")
        
        if password != confirm:
            request.session['reset_error'] = "Passwords do not match"
        elif code != request.session.get('reset_code'):
            request.session['reset_error'] = "Invalid code"
        else:
            email = request.session.get('reset_email')
            username = request.session.get('reset_username')
            
            if not email or not username:
                request.session['reset_error'] = "Session expired. Please start over."
            else:
                try:
                    user = User.objects.get(email=email, username=username)
                    user.set_password(password)
                    user.save()
                    request.session['reset_success'] = f"Password changed for user '{username}'. Please login."
                    request.session['open_login_modal'] = True
                    # Clear reset session data
                    request.session.pop('reset_code', None)
                    request.session.pop('reset_email', None)
                    request.session.pop('reset_username', None)
                    request.session.pop('reset_step', None)
                except User.DoesNotExist:
                    request.session['reset_error'] = f"No user found with email '{email}' and username '{username}'. Please check and try again."
        return redirect('home')
    return redirect('home')


# def send_reset_code(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         username = request.POST.get("username")
#         try:
#             user = User.objects.get(email=email, username=username)
#             code = str(random.randint(100000, 999999))
#             request.session['reset_code'] = code
#             request.session['reset_email'] = email
#             request.session['reset_username'] = username
#             send_mail(...)
#             request.session['reset_step'] = 2
#             request.session['reset_success'] = "Code sent to your email."
#         except User.DoesNotExist:
#             request.session['reset_error'] = f"No account with email '{email}' and username '{username}'."
#         return redirect('home')
#     return redirect('home')


from django.core.mail import send_mail
from django.conf import settings

def send_reset_code(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        try:
            user = User.objects.get(email=email, username=username)
            code = str(random.randint(100000, 999999))
            request.session['reset_code'] = code
            request.session['reset_email'] = email
            request.session['reset_username'] = username
            
            # Correct send_mail call
            send_mail(
                subject="Your password reset code",
                message=f"Your code is: {code}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            
            request.session['reset_step'] = 2
            request.session['reset_success'] = "Code sent to your email."
        except User.DoesNotExist:
            request.session['reset_error'] = f"No account with email '{email}' and username '{username}'."
        return redirect('home')
    return redirect('home')