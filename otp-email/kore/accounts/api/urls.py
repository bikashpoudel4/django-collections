from django.urls import path
# from .views import LoginAPIView, RegistrationAPIView, VerifyOTPView, ForgotPasswordView
# from .views import ResentOtpView
from .views import *

app_name='accounts'

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='user-registration'), ## User Registeration
    path("userdetail/<int:pk>/", UserprofileDetailAPIView.as_view(), name="user-detail"),
    
    path('resendotp/', ResentOtpView.as_view(), name='resend-otp'), ## User Login after otp verification
    path('login/', LoginAPIView.as_view(), name='login-user'), ## User Login after otp verification
    
    path('verify/', VerifyOTPView.as_view(), name='verify-otp'), ## Verify OTP
    path('forgotpassword/', ForgotPasswordView.as_view(), name='forgot-password'), #forgot Password
    ]