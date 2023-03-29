from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.fields import EmailField
from rest_framework.response import Response
from rest_framework.views import APIView
import pyotp
import random
import jwt
from django.conf import settings
from django.core.mail import send_mail
from accounts.models import UserProfiile
from .serializers import LoginSerializer, RegistrationSerializer, VerifyOTPSerializer, ForgotPasswordSerializer, ResetPasswordSerializer
from django.contrib.auth import authenticate
from passlib.hash import django_pbkdf2_sha256 as handler
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from django.core.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import update_last_login

from .serializers import *
from rest_framework.generics import get_object_or_404
from rest_framework.generics import UpdateAPIView


# Methot to Generate OTP using pyotp
# generate TOTP
def generateOTP():
    global totp
    secret = pyotp.random_base32()
    # set interval(time of the otp expiration) according to your need in seconds.
    totp = pyotp.TOTP(secret, interval=300)
    one_time = totp.now()
    # print("totp-------" , one_time)
    return one_time

# Method for Verifying OTP
# need to wait few seconds for initially server to verify
def verifyOTP(one_time):
    answer = totp.verify(one_time)
    return answer


"""Registration API view User registration form, send email containing email.
"""
class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    # def get(self, request):
    #     return Response({'Status': 'You are not allowed to view other users.'})
    
        # get method
    def get(self, request):
        # creating note object
        userObject = UserProfiile.objects.all()
        serializerClass = RegistrationSerializer(userObject, many=True) #many=True is essentiaol here
        return Response(serializerClass.data)

    def post(self, request):
        # serializer_class = RegistrationSerializer(data=requset.data)
        email = request.data['email']
        # print(email) ## Console LOG
        data = UserProfiile.objects.filter(email=email)
        # print('data ', data)

        if data.exists():
            return Response({'msg': 'This email is already taken.'}, status=status.HTTP_409_CONFLICT)
        else:
            serializer = self.serializer_class(data=request.data)
            # print("user", serializer)
            first_name = request.data['first_name']

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                message = f'Welcome {first_name}. We need to verify your OTP for account activation. Your OTP is : ' + \
                    generateOTP()
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                message = message
                subject = "OTP - Bikash Poudel Email" 
                send_mail(
                    subject,
                    message,
                    email_from,
                    recipient_list,
                    fail_silently=False,
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"Error": "Sign Up Failed"}, status=status.HTTP_400_BAD_REQUEST)

"""
Retrieve, Update, Patch Update and Delete a user's instance
"""
class UserprofileDetailAPIView(APIView):
    # """Method 2 for get_object"""
    def get_object(self,pk):
        userObj = get_object_or_404(UserProfiile, pk=pk)
        return userObj

    def get(self, request, pk):
        userObj = self.get_object(pk)
        serializerClass = RegistrationSerializer(userObj)
        return Response(serializerClass.data)

    def put(self, request, pk):
        userObj = self.get_object(pk)
        serializerClass = RegistrationSerializer(userObj, data=request.data)
        if serializerClass.is_valid():
            serializerClass.save()
            return Response(serializerClass.data)
        return Response(serializerClass.errors, status=status.HTTP_400_BAD_REQUEST)    
        
    def patch(self, request, pk):
        userObj = self.get_object(pk)
        serializerClass = RegistrationSerializer(userObj, data=request.data, partial=True)
        if serializerClass.is_valid():
            serializerClass.save()
            return Response(serializerClass.data)
        return Response(serializerClass.errors, status=status.HTTP_400_BAD_REQUEST)  

    def delete(self, request, pk):
        userObj = self.get_object(pk)
        userObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ResentOtpView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ResendOtpSerializer
    def post(self, request):
        email = request.data['email']
        users= UserProfiile.objects.get(email=email)
        if users.is_confirmed==True:
            # print("inside already verified")
            return Response({"Error": "Already verified"}, status=status.HTTP_409_CONFLICT)
        else:
            # print("out of if verified")
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                email = request.data['email']
                # print(email)
                UserProfiile.objects.filter(email=email)
                message = f'Welcome {email}. We need to verify your OTP for account activation. Your OTP is : ' + \
                        generateOTP()
                email_from = settings.EMAIL_HOST_USER
                # print(message, "-------mmmmmmmmmmmmmmmm---------")
                recipient_list = [email]
                message = message
                subject = "OTP - Bikash Poudel Email" 
                send_mail(
                    subject,
                    message,
                    email_from,
                    recipient_list,
                    fail_silently=False,
                    )

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"Error": "Verification Failed !"}, status=status.HTTP_400_BAD_REQUEST)
        

## Resend otp ends

"""Verifying OTP"""
class VerifyOTPView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = VerifyOTPSerializer

    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        email = request.data['email']
        one_time = request.data['otp']
        # print('one_time_password', one_time)
        one = verifyOTP(one_time)
        # print('one-----------', one)
        if one:
            UserProfiile.objects.filter(email=email).update(
                is_confirmed=True, is_used=True, otp=one_time)
            # print("if one------", one)
            
            if serializer.is_valid():
                print("-------------------------------")
                email = request.data['email']
                print(email)
                UserProfiile.objects.filter(email=email)

                subject = 'Bikash Poudel Email'
                message = 'You are ready to use your account.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                print(recipient_list)

                send_mail(
                    subject,
                    message,
                    email_from,
                    recipient_list,
                    fail_silently=False,
                )
            
            return Response({'message': 'OTP verfication successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'OTP verfication Failed'}, status=status.HTTP_400_BAD_REQUEST)

"""Forget Password
generates random password and sends email to the user.
"""
class ForgotPasswordView(APIView):
    serializer_class = ForgotPasswordSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        # Generating Random Password
        str_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
        str_2 = ['!', '@', '#', '$', '%', '&', '*', '/', '-', '+']
        str_3 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        str = random.choice(str_1)
        for s in range(4):
            str += random.choice(str_1).lower()
        str += random.choice(str_2)
        for x in range(2):
            str += random.choice(str_3)

        password = handler.hash(str)

        if serializer.is_valid():
            email = request.data['email']
            # print(email)
            UserProfiile.objects.filter(email=email).update(password=password)

            subject = 'Forgot Password Request - Bikash Poudel Email'
            message = 'Your request for Forgot Password has been received, your new password is ' + str
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]

            send_mail(
                subject,
                message,
                email_from,
                recipient_list,
                fail_silently=False,
            )
            return Response({'message': 'New random generated password is sent to your email.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Not a valid request'}, status=status.HTTP_400_BAD_REQUEST)

#######################--on Progress----######################################
# class ResetPasswordView(UpdateAPIView):
#     serializer_class = ResetPasswordSerializer
#     model = MyUser
#     permission_classes = (IsAuthenticated,)

#     def get_object(self, queryset=None):
#         obj = self.request.user
#         return obj
    
#     def update(self, request, *args, **kwargs):
#     # def update(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             # Check old password
#             if not self.object.check_password(serializer.data.get("old_password")):
#                 return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            
#             # confirm the new passwords match
#             new_password = serializer.data.get("new_password")
#             confirm_password = serializer.data.get("confirm_password")
#             if new_password != confirm_password:
#                 return Response({"new_password": ["New passwords must match"]}, status=status.HTTP_400_BAD_REQUEST)
#         #     # set_password also hashes the password that the user will get
#             self.object.set_password(serializer.data.get("new_password"))
#             self.object.save()
#             response = {
#                 'status': 'success',
#                 'code': status.HTTP_200_OK,
#                 'message': 'Password updated successfully',
#                 'data': []
#             }
#             return Response(response)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

######################################################


"""Login View"""
class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']
        # print('email', email)
        filter_data = UserProfiile.objects.filter(email=email).values('is_active')
        # print('filter_data', filter_data)
        if filter_data.exists():
            val = filter_data[0]['is_active']
        else:
            return Response("Email not registered.", status=status.HTTP_400_BAD_REQUEST)

        if val:
            if serializer.is_valid():
                user = authenticate(
                    username=request.data['email'], password=request.data['password'])
                update_last_login(None, user)
                if user is not None and user.is_confirmed and user.is_active:  ## we can change this accordind to need
                    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                    payload = jwt_payload_handler(user)
                    token = jwt_encode_handler(payload)
                    return Response({'message': 'Login successful', 'is_confirmed': user.is_confirmed, 'token': token,
                                     'first_name': user.first_name, 'last_name': user.last_name,
                                     }, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Account not approved or wrong Password.'}, status=status.HTTP_409_CONFLICT)
            else:
                return Response({'message': 'Invalid data'}, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response({'Error': 'Not a valid user'}, status=status.HTTP_401_UNAUTHORIZED)
