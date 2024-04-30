from django.urls import path
from .views import signUp, login,logout,mypage,mypageUpdate,main


app_name='account'

urlpatterns = [
    path('signup/', signUp, name='signUp'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('mypage/', mypage, name='mypage'),
    path('mypageUpdate/', mypageUpdate, name='mypageUpdate'),
]