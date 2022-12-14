#-----------------------------------#
# Developed by: Tech With Tim
# GitHub Author: https://github.com/techwithtim/Music-Controller-Web-App-Tutorial
# Adapted by: Thiag Piovesan
# My GitHub: https://github.com/ThiagoPiovesan/ThiagoPiovesan
#-----------------------------------#

# Libs Importantion:
from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
    