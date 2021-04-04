from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from .serializer import (UserSerializer,ResetPasswordSerializer,
TokenBlackListSerializer, HandleResetPasswordSerializer)
from core.settings import SECRET_KEY
import jwt
from .models import NewUser
from core.tasks import send_mail



class RegisterationView(generics.GenericAPIView):

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = NewUser.objects.get(email=serializer.data['email'])
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        link = "/api/v1/verify-email/"
        url = 'http://'+current_site+link+"?token="+str(token)
        email_body = 'Hi '+user.username +'\n' + \
            'You can verify your email with this link: \n' + url

        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Email Verification'}
        
        send_mail(data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class VerifyEmail(generics.GenericAPIView):

    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
            user = NewUser.objects.get(id=payload['user_id'])
            user.is_verified = True
            user.save()

            return Response({'email': 'Succesfully activated!'}, 
            status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation expired.'}, 
            status=status.HTTP_400_BAD_REQUEST)

        except jwt.DecodeError as identifier:
            return Response({'error': 'Invalid token.'}, 
            status=status.HTTP_400_BAD_REQUEST)



class ResetPassword(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = NewUser.objects.get(email=serializer.data['email'])
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        link = "/api/v1/changepassword/"
        url = 'http://'+current_site+link+"?token="+str(token)
        email_body = 'Hi '+user.username +'\n' + \
            'Use this link if you want to change your password: \n' + url

        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Rest Password'}
        
        send_mail(data)
        return Response("Email sent successfully.", status=status.HTTP_202_ACCEPTED)



class HandleResetPassword(generics.GenericAPIView):
    serializer_class = HandleResetPasswordSerializer

    def post(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")

        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation expired.'}, 
            status=status.HTTP_400_BAD_REQUEST)

        except jwt.DecodeError as identifier:
            return Response({'error': 'Invalid token.'}, 
            status=status.HTTP_400_BAD_REQUEST)

        user = NewUser.objects.get(id=payload['user_id'])
        user.set_password(request.data['password'])
        user.save()
        return Response({'email': 'Password changed Successfully!'}, 
        status=status.HTTP_200_OK)

 



class LogOut(generics.GenericAPIView):
    serializer_class = TokenBlackListSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args):
        sz = self.get_serializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()
        return Response(status=status.HTTP_204_NO_CONTENT)