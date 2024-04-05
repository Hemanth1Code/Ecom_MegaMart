from django.urls import path

from projectStore.views import *

urlpatterns = [
    path('',home,name='homee'),
    path('cart',cartPage),
    path('checkout',checkout),

    path('loginn',user_login,name="login"),
    path('sign',user_signup,name="register"),
    path('logout',user_logout,name="logout"),


    path('new',newColl),
    path('women',womenColl),
    path('men',menColl),
    path('kids',kidsColl),
    path('motorsport',motorSportColl),
    path('sportt',sportColl),



]