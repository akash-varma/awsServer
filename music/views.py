#music

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
     return HttpResponse("<h1>music app home page</h1>")
     
def details(request, album_id):
     return HttpResponse("<h2> albumn id is : " + str(album_id) + "</h2>")





     
