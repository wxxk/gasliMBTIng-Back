from django.shortcuts import render
from .models import Friend
from .serializers import FriendSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# 친구 목록 조회 - 로그인 필요
@api_view(['GET'])
@permission_classes([AllowAny])
def friends_list(request):
    friends = Friend.objects.filter(user=request.user)
    serializer = FriendSerializer(friends, many=True)
    return Response(serializer.data)

# 친구 목록 필터 - 로그인 필요
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def friends_filter(request,filter):
#     friends = Friend.objects.filter(group=filter)
#     serializer = FriendSerializer(friends, many=True)
#     return Response(serializer.data)
@api_view(['POST'])
@permission_classes([AllowAny])
def friends_filter(request):
    print(request.data)
    friends = Friend.objects.filter(group=request.data['filter'])
    serializer = FriendSerializer(friends, many=True)
    return Response(serializer.data)

# 친구 생성 - 로그인 필요
@api_view(['POST'])
@permission_classes([AllowAny])
def friends_create(request):
    print(request.user)
    serializer = FriendSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.validated_data['user'] = request.user
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 친구 상세 내용 확인 - 로그인 필요
@api_view(['GET'])
@permission_classes([AllowAny])
def friends_detail(request, pk):
    try:
        friend = Friend.objects.get(pk=pk)
    except Friend.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = FriendSerializer(friend)
    return Response(serializer.data)
    
# 친구 수정 - 로그인 필요
@api_view(['PUT'])
@permission_classes([AllowAny])
def friends_update(request, pk):
    friend = Friend.objects.get(pk=pk)
    serializer = FriendSerializer(friend, request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 친구 삭제 - 로그인 필요
@api_view(['DELETE'])
@permission_classes([AllowAny])
def friends_delete(request, pk):
    friend = Friend.objects.get(pk=pk)
    friend.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
