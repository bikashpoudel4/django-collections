from datetime import datetime
from rest_framework import serializers
from django.contrib.auth import authenticate
from accounts.models import UserProfiile
from django.utils.text import gettext_lazy as _
from django.contrib.auth import password_validation
from django.contrib.auth.password_validation import validate_password


class RegistrationSerializer(serializers.ModelSerializer):
    # user_id = serializers.UUIDField()
    password = serializers.CharField(help_text=_("Password"), 
                                     max_length=128, min_length=8, 
                                     required=True, write_only=True, 
                                     style={'input_type': 'password'})
    
    password2 = serializers.CharField(help_text=_("Re-Password"), 
                                     max_length=128, min_length=8, 
                                     required=True, write_only=True, 
                                     style={'input_type': 'password'})

    class Meta:
        model = UserProfiile
        fields = ['first_name', 'last_name',
                  'username', 'email',
                  'mobile', 'city', 'birth_date',
                  'password', 'password2',
                  'user_id',
                  ]
        
    def save(self):
        user = UserProfiile(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            mobile=self.validated_data['mobile'],
            city=self.validated_data['city'],
            birth_date=self.validated_data['birth_date'],
            )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user
    #######################################################
    
## Resend otp
class ResendOtpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = UserProfiile
        fields = ['email']


class VerifyOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfiile
        fields = ['otp', 'email']


class ForgotPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = UserProfiile
        fields = ('email',)


class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    old_password = serializers.CharField(help_text=_("Current Password"), 
                                         max_length=128, min_length=8, 
                                         required=True,
                                         write_only=True, style={'input_type': 'password'})
    new_password = serializers.CharField(help_text=_("New Password"), 
                                         max_length=128, min_length=8, 
                                         required=True,
                                         write_only=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(help_text=_("Confirm new Password"), 
                                         max_length=128, min_length=8, 
                                         required=True,
                                         write_only=True, style={'input_type': 'password'})
        
    class Meta:
        model = UserProfiile
        fields = ('email', 'old_password', 'new_password', 'confirm_password')



class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    # username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(help_text=_("Password"), 
                                     max_length=128, min_length=8, 
                                     required=True, write_only=True, 
                                     style={'input_type': 'password'})
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        fields = ('email','password','token')
    ## We  validate for login as below
    # def validate(self, data):

    #     email = data.get('email', None)
    #     password = data.get('password', None)
    #     if email is None:
    #         raise serializers.ValidationError(
    #             'An email address is required to log in.'
    #         )

    #     if password is None:
    #         raise serializers.ValidationError(
    #             'A password is required to log in.'
    #         )

    #     user = authenticate(username=email, password=password)

    #     # if not user.is_active:
    #     #     raise serializers.ValidationError(
    #     #         'This user has been deactivated.'
    #     #     )

    #     return {
    #         'email': user.email,
    #         'token': user.token
    #     }
