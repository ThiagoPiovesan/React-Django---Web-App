#-----------------------------------#
# Developed by: Tech With Tim
# GitHub Author: https://github.com/techwithtim/Music-Controller-Web-App-Tutorial
# Adapted by: Thiag Piovesan
# My GitHub: https://github.com/ThiagoPiovesan/ThiagoPiovesan
#-----------------------------------#

# Libs Importantion:
from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def main(request):
    return HttpResponse("<h1>Hello<h1>")