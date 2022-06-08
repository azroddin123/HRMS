from rest_framework import serializers
from .models import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    class Meta:
        model = MyUser
        fields = ['id',"email", "role", "password", "password2","name"]
        
    def save(self):
        print(self.validated_data)
        user = MyUser(email=self.validated_data["email"])
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if (password and password2) and password != password2:
            raise serializers.ValidationError(
                {"password": "password fields does not match"}
            )
        role = self.validated_data["role"]
        name = self.validated_data['name']
        user.role=role
        user.name=name
        user.set_password(password)
        user.save()
        return user
