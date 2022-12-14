from django.shortcuts import render
from .models import Mbti
from .serializers import MbtiSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


@api_view(["GET"])
@permission_classes([AllowAny])
def mbti_list(request):
    if request.method == "GET":
        mbti = Mbti.objects.all()
        serializer = MbtiSerializer(mbti, many=True)

        return Response(serializer.data)

    # elif request.method == "POST":
    #     serializer = MbtiSerializer(data=request.data)

    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

    #     JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(["GET"])
@permission_classes([AllowAny])
def mbti_details(request, pk):
    try:
        mbti = Mbti.objects.get(pk=pk)

    except Mbti.DoseNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = MbtiSerializer(mbti)
        return Response(serializer.data)

    # elif request.method == "PUT":
    #     serializer = MbtiSerializer(mbti, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    # elif request.method == "DELETE":
    #     mbti.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)