#-----------------------------------#
# Developed by: Tech With Tim
# GitHub Author: https://github.com/techwithtim/Music-Controller-Web-App-Tutorial
# Adapted by: Thiag Piovesan
# My GitHub: https://github.com/ThiagoPiovesan/ThiagoPiovesan
#-----------------------------------#

# Libs Importantion:
from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')