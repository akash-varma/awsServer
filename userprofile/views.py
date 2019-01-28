#user profile

from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import UserList

# Create your views here.
def myFun(request):
     total_users = UserList.objects.all()
     context = {
          'total_users' : total_users
     }
     return render(request, 'userprofile/index.html', context)

def userDetails(request, user_id):
     try :
          users = UserList.objects.get(pk=user_id)
     except UserList.DoesNotExist:
          raise Http404("user does not exist")
     return render(request, 'userprofile/details.html', {'users':users})

