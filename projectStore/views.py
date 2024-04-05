from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

from django.contrib.auth import login,logout,authenticate
#home view

def home(request):
    categoryID = request.GET.get('category')
    categoryInfo = Category.objects.all()
    if categoryID:
        productInfo = Product.get_category_Info(categoryID)
    else:
      productInfo= Product.objects.all()
    context = {'productInfo':productInfo,'categoryInfo':categoryInfo}

    return render(request,'homePage.html',context)



def cartPage(request):
   return render(request,'cart.html')

def checkout(request):
   context = {}
   return render(request,'checkout.html',context)

def user_signup(request):
   context ={}
   return render(request,'bsignUp.html',context)
def user_login(request):
         context ={}
         return render(request,'blogin.html',context)

def user_logout(request):
    logout(request)
    return redirect('register')

def newColl(request):
   newCollInfo = NewCollection.objects.all()
   context = {'newCollInfo':newCollInfo}
   return render(request,'aNewColl.html',context)

def womenColl(request):
   context = {}
   return render(request,'aWomenColl.html',context)

def menColl(request):
   context = {}
   return render(request,'aMenColl.html',context)

def kidsColl(request):
   context = {}
   return render(request,'aKidsColl.html',context)

def motorSportColl(request):
   context = {}
   return render(request,'aMotorSportColl.html',context)

def sportColl(request):
   context = {}
   return render(request,'aSportColl.html',context)