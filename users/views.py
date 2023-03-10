from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserValidationSerializer, UserLoginSerializer, ConfirmCodeSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from users.models import ConfirmCode
from rest_framework.views import APIView
import random


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserValidationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        confirm_code = random.randint(100000, 999999)
        user = User.objects.create_user(username=serializer.validated_data.get('username'),
                                        password=serializer.validated_data.get('password'),
                                        is_active=False)
        ConfirmCode.objects.create(user=user, code=confirm_code)
        return Response({"confirmation_code": confirm_code}, status=status.HTTP_201_CREATED)


class ConfirmAPIView(APIView):
    def post(self, request):
        serializer = ConfirmCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            confirm_code = ConfirmCode.objects.get(code=serializer.validated_data.get('code'))
        except ConfirmCode.DoesNotExist:
            return Response({"detail": "Invalid username or confirm code"}, status=status.HTTP_400_BAD_REQUEST)
        user = confirm_code.user
        user.is_active = True
        user.save()
        confirm_code.delete()
        return Response({"message": "User registration confirmed successfully"}, status=status.HTTP_200_OK)


class AuthorizationAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data.get('username'),
                            password=serializer.validated_data.get('password'))

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)
