from rest_framework import serializers
from .models import Community, Comment
from accounts.serializers import UserSerializer


class CommunitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Community
        read_only_fields = (
            "created_at",
            "updated_at",
            "like",
            # "user",
        )
        fields = (
            "id",
            "category",
            "title",
            "mbti",
            "content",
            "user",
            "created_at",
            "updated_at",
            "like",
            "image",
        )


class CommentSerializer(serializers.ModelSerializer):
    comment_user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        read_only_fields = ("created_at",)
        fields = "__all__"


class RecommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
