from django.shortcuts import render
from .models import Community, Comment, Photo
from .serializers import CommunitySerializer, CommentSerializer, RecommentSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# 글 목록 조회 - 로그인 없이 조회 가능
@api_view(['GET'])
@permission_classes([AllowAny])
def community_list(request):
    community = Community.objects.all()
    serializer = CommunitySerializer(community, many=True)
    return Response(serializer.data)

# 글 생성 - 로그인 필요
@api_view(['POST'])
@permission_classes([AllowAny])
def community_create(request):
    serializer = CommunitySerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.validated_data['user'] = request.user
        serializer.save()

        for img in request.FILES.getlist("imgs"):
                # Photo 객체를 하나 생성한다.
                photo = Photo()
                # 외래키로 현재 생성한 community 글의 기본키를 참조한다.
                photo.community = serializer
                # imgs로부터 가져온 이미지 파일 하나를 저장한다.
                photo.image = img
                # 데이터베이스에 저장
                photo.save()
        print(serializer.data, type(serializer.data))
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 글 상세 내용 확인 - 로그인 필요
@api_view(['GET'])
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
@api_view(['PUT'])
def community_update(request, pk):
    community = Community.objects.get(pk=pk)
    if community.user == request.user:
        serializer = CommunitySerializer(community, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 글 삭제 - 로그인 필요
@api_view(['DELETE'])
def community_delete(request, pk):
    community = Community.objects.get(pk=pk)

    if community.user == request.user:
        community = Community.objects.get(pk=pk)
        
        community.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# (테스트 확인용) 댓글, 대댓글 목록 확인하기 - 로그인 필요
@api_view(['GET'])
def comment_list(request):
    comment = Comment.objects.all()
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data)

# 댓글 작성하기 - 로그인 필요
@api_view(['POST'])
def comment_create(request, community_pk):
    community = Community.objects.get(pk=community_pk)
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.validated_data['article'] = community
        serializer.validated_data['comment_user'] = request.user
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# (테스트 확인용) 대댓글 목록 확인하기 - 로그인 필요
@api_view(['GET'])
def recomment_list(request):
    recomment = Comment.objects.exclude(parent_comment_id=None)
    serializer = CommentSerializer(recomment, many=True)
    return Response(serializer.data)

# 대댓글 작성하기 - 로그인 필요
@api_view(['POST'])
def recomment_create(request, community_pk, comment_pk):
    community = Community.objects.get(pk=community_pk)
    serializer = RecommentSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.validated_data['article'] = community
        serializer.validated_data['comment_user'] = request.user
        serializer.validated_data['parent_comment_id'] = comment_pk
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)