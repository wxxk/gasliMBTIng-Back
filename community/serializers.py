from rest_framework import serializers
from .models import Community, Comment, Notification
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


class NotificationSerializer(serializers.ModelSerializer):
    community = CommunitySerializer(read_only=True)
    comment = CommentSerializer(read_only=True)
    send_user = UserSerializer(read_only=True)
    receive_user = UserSerializer(read_only=True)
    is_read = serializers.ReadOnlyField()
    class Meta:
        model = Notification
        fields = "__all__"