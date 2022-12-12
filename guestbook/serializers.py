from rest_framework import serializers
from .models import Guestbook

class GuestbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guestbook
        fields = '__all__'

        