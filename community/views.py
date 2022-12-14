from .models import Community, Comment, Notification
from .serializers import CommunitySerializer, CommentSerializer, RecommentSerializer,NotificationSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# 글 목록 조회 - 로그인 없이 조회 가능
@api_view(["GET"])
@permission_classes([AllowAny])
def community_list(request):
    community = Community.objects.all()
    serializer = CommunitySerializer(community, many=True)
    return Response(serializer.data)


# 글 생성 - 로그인 필요
@api_view(["POST"])
@permission_classes([AllowAny])
def community_create(request):
    serializer = CommunitySerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.validated_data["user"] = request.user
        print(serializer.validated_data["title"])
        print(serializer.validated_data["content"])
        print(serializer.validated_data["image"])
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 글 상세 내용 확인 - 로그인 필요
@api_view(["GET"])
def community_detail(request, pk):
    try:
        community = Community.objects.get(pk=pk)
    except Community.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CommunitySerializer(community)
    return Response(serializer.data)


# 좋아요
def like(request, community_pk):
    community = Community.objects.get(pk=community_pk)

    if community.like.filter(pk=request.user.pk).exists():
        community.like.remove(request.user)
        is_likes = False
    else:
        community.like.add(request.user)
        is_likes = True
    data = {"is_likes": is_likes, "likes_count": community.like.count()}
    return Response(data)


# 글 수정 - 로그인 필요
@api_view(["PUT"])
def community_update(request, pk):
    community = Community.objects.get(pk=pk)
    if community.user == request.user:
        serializer = CommunitySerializer(community, request.data)

        print(serializer)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 글 삭제 - 로그인 필요
@api_view(["DELETE"])
def community_delete(request, pk):
    community = Community.objects.get(pk=pk)

    if community.user == request.user:
        community = Community.objects.get(pk=pk)

        community.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# (테스트 확인용) 댓글, 대댓글 목록 확인하기 - 로그인 필요
@api_view(["GET"])
def comment_list(request, community_pk):
    comments = Comment.objects.filter(article=community_pk)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


# 댓글 작성하기 - 로그인 필요
@api_view(["POST"])
def comment_create(request, community_pk):
    community = Community.objects.get(pk=community_pk)
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.validated_data["article"] = community
        serializer.validated_data["comment_user"] = request.user
        serializer.save()
        new_comment = Comment.objects.all()[0]
        Notification.objects.create(
                send_user=request.user,
                receive_user=community.user,
                community=community,
                comment=new_comment
            )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["DELETE"])
def comment_delete(request, community_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    print(request.user.id)
    print(comment.comment_user_id)

    if comment.comment_user_id == request.user.id:
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# (테스트 확인용) 대댓글 목록 확인하기 - 로그인 필요
@api_view(["GET"])
def recomment_list(request):
    recomment = Comment.objects.exclude(parent_comment_id=None)
    serializer = CommentSerializer(recomment, many=True)
    return Response(serializer.data)


# 대댓글 작성하기 - 로그인 필요
@api_view(["POST"])
def recomment_create(request, community_pk, comment_pk):
    community = Community.objects.get(pk=community_pk)
    serializer = RecommentSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.validated_data["article"] = community
        serializer.validated_data["comment_user"] = request.user
        serializer.validated_data["parent_comment_id"] = comment_pk
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# community 필터결과 보여주기
@api_view(["GET"])
@permission_classes([AllowAny])
def community_filter(request,data):
    data=data.split('&')
    if data[0]=='free':
        data[0] = '자유'
    elif data[0]=='counsel':
        data[0] = '상담'
    elif data[0] =='discussion':
        data[0] = '토론'
    elif data[0] =='question':
        data[0] = '질문'

    category = data[0]
    mbti = data[1]

    if data[0]=='all' and data[1]=='all':
        community = Community.objects.all()
    elif data[0]=='all':
        community = Community.objects.filter(mbti=mbti)
    elif data[1]=='all':
        community = Community.objects.filter(category=category)
    else:
        community = Community.objects.filter(category=category, mbti=mbti)
    serializer = CommunitySerializer(community, many=True)
    return Response(serializer.data)

# 알림 조회
@api_view(["GET"])
@permission_classes([AllowAny])
def notification_list(request):
    print("들어왓다")
    notifications = Notification.objects.filter(receive_user_id=request.user.pk, is_read=0)
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)

# 알림 읽음처리
@api_view(["PUT"])
@permission_classes([AllowAny])
def is_read(request, pk):
    notification = Notification.objects.get(pk=pk)
    notification.is_read = 1
    notification.save()
    serializer = NotificationSerializer(notification)
    return Response(serializer.data)

@api_view(["PUT"])
@permission_classes([AllowAny])
def all_read(request):
    notifications = Notification.objects.filter(receive_user=request.user)
    for notification in notifications:
        notification.is_read = 1
        notification.save()
    serializer = NotificationSerializer(notifications)
    return Response(serializer.data)