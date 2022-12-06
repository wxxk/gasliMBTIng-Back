from rest_framework import serializers
from .models import Community, Comment, Photo

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class RecommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'