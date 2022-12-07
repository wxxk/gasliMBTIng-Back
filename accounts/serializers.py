from .models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

        extra_kwargs = {
            'password' : {'write_only' : True }
        }
    
    def create(self,validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None :
            #provide django, password will be hashing!
            instance.set_password(password)
        instance.save()
        return instance