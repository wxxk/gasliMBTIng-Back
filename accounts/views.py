from django.shortcuts import render
from .models import User
from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# Create your views here.
@api_view(['GET'])
def user_detail(request):
    try:
        user = User.objects.get(pk=request.user.pk)
        print(user)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response(serializer.data)