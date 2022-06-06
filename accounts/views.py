from django.shortcuts import render
from yaml import serialize

from .serializers import MyUserSerializer
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from rest_framework import status, permissions

from random import randint
import datetime
from datetime import timedelta
import jwt
from django.conf import settings


# def create_token(user):
#     payload = {
#         'id': user_id,
#         'exp' = datetime.datetime.utcnow() + datetime.timedelta(hours=24)
#         'iat' = datetime.datetime.utcnow()
#     }

#     token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")

#     return token


# Create your views here.
MyUser = get_user_model()

class RegisterApi(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserApi(APIView):
    def get(self, request, *args, **kargs):
        users = MyUser.objects.all()
        serializer = MyUserSerializer(users, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginApi(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        print(email, password)
        user = MyUser.objects.filter(email=email).first()
        print(user)
        if user is None:
            return Response(
                {"status": 404, "message": "User is not registered"},
                status=status.HTTP_404_NOT_FOUND,
            )
            # raise exceptions.AuthenticationFailed("Invalid Credentials")
        if not user.check_password(raw_password=password):
            return Response(
                {"status": 400, "message": "Wrong Password"},
                status=status.HTTP_400_BAD_REQUEST,
            )
            # raise exceptions.AuthenticationFailed("Invalid Credentials")
        # token = create_token(user_id=user.id)
        serializer = MyUserSerializer(user)
        return Response(
            {
                "message": "User logged in successfully",
                "user_info": serializer.data,
                "access_token": token,
            },
            status=status.HTTP_200_OK,
        )
