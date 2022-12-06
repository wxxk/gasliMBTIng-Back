from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

from accounts.serializers import UserSerializer

from rest_framework.authtoken.models import Token



@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    nickname = request.data.get('nickname')

    serializer = UserSerializer(data=request.data)
    serializer.username = username
    serializer.nickname = nickname

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(password)
        user.save()

    # token = Token.objects.create(user)
    # return Response({"Token": token.key})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=username, password=password)

    if user is None:
        return Response({'message': '아이디 또는 비밀번호가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

    print(username,password)
    refresh = RefreshToken.for_user(user)
    update_last_login(None, user)

    return Response({'refresh_token': str(refresh),
                     'access_token': str(refresh.access_token), }, status=status.HTTP_200_OK)