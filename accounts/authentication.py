from django.conf import settings
from rest_framework import authentication, exceptions
from rest_framework.authentication import BaseAuthentication
import jwt

from . import models

class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # return super().authenticate(request)
        token = request.COOKIES.get("jwt")
        # print('Cookie Recieved-----',token)
        if not token:
            raise exceptions.AuthenticationFailed("Credentials Not Found ..Please Login ")
        try: 
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=['HS256'])
        except:
            raise exceptions.AuthenticationFailed("Unauthorized")
        user = models.MyUser.objects.filter(id=payload["id"]).first()
        return (user, None)
