from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import  RegisterUserSerializer



class CustomUserCreate( APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        reg_serializer = RegisterUserSerializer( data= request.data)
        if reg_serializer.is_valid():
            newuser= reg_serializer.save()
            if newuser:
                return Response(status= status.HTTP_201_CREATED)
            else:
                return Response({'message':"user already exist."})
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

