from rest_framework import serializers
from .models import Mbti
from accounts.serializers import UserSerializer

class MbtiSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    class Meta:
        model = Mbti
        fields = '__all__'