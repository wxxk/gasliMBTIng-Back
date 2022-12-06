from rest_framework import serializers
from .models import Mbti

class MbtiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mbti
        fields = '__all__'