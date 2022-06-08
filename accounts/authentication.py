from django.conf import settings
from rest_framework import authentication, exceptions
from rest_framework.authentication import BaseAuthentication
import jwt

from . import models

class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # return super().authenticate(request)
        print("in serializer")
        token = request.headers.get('Authorization')
        print("token is : ",token)
        if not token:
            raise exceptions.AuthenticationFailed("Credentials Not Found ..Please Login")
        
        try: 
            payload = jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
            print(payload['email'])
            # payload = jwt.decode(token, settings.JWT_SECRET, algorithms=['HS256'])
        except:
            raise exceptions.AuthenticationFailed("Unauthorized")
        
        user = models.MyUser.objects.filter(email=payload["email"]).first()
        return (user, None)
