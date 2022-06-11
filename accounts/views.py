from django.conf import settings
from .serializers import MyUserSerializer
from .models import *
from accounts.authentication import CustomAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import jwt
from . import authentication


def generate_token(email) : 
    payload = {
        'email' : email
    }
    token = jwt.encode(payload,settings.SECRET_KEY,algorithm="HS256")
    return token


class RegisterApi(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            token = generate_token(request.data['email'])
            return Response(data = { "data" : serializer.data , "token" :  token }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginApi(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        print(email, password)
        user = MyUser.objects.filter(email=email).first()
        if not user : 
            return Response({"data" : "User Not Exists"},status=status.HTTP_200_OK)
        print("user is",user.email)
        token = generate_token(user.email)
        print(token)
        
        if user is None:
            return Response({"message": "User is not registered"},status=status.HTTP_404_NOT_FOUND,)
        
        # if not user.check_password(raw_password=password):
        #     return Response({"status": 400, "message": "Wrong Password"},status=status.HTTP_400_BAD_REQUEST)
        serializer = MyUserSerializer(user)
        return Response({"message": "User logged in successfully","user_info": serializer.data,"token" : token },status=status.HTTP_200_OK,)


class UserApi(APIView):
    authentication_classes = [CustomAuthentication]
    def get(self, request, *args, **kargs):
        user = request.user
        serializer = MyUserSerializer(user)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    

    # def put(self, request, id, *args, **Kwargs):
    #     user = MyUser.objects.get(id=id)
    #     if not user:
    #         return Response("user not found")
    #     print(request.data)
    #     serializer = MyUserSerializer(user, data=request.data)
    #     if serializer.is_valid():
    #         return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
    #     return Response(error=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


