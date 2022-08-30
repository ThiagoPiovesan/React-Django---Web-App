#-----------------------------------#
# Developed by: Tech With Tim
# GitHub Author: https://github.com/techwithtim/Music-Controller-Web-App-Tutorial
# Adapted by: Thiag Piovesan
# My GitHub: https://github.com/ThiagoPiovesan/ThiagoPiovesan
#-----------------------------------#

# Libs Importantion:
from django.urls import path
from .views import RoomView

urlpatterns = [
    path('room', RoomView.as_view()),

]
