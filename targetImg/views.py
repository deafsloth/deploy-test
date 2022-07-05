from typing import Reversible
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .serializers import TargetImgSerializer
from .models import TargetImg

class TargetImgListAPI(APIView):
    def get(self, request):
        targetImgs = TargetImg.objects.all()
        serializer = TargetImgSerializer(targetImgs, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = TargetImgSerializer(
            data = request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
