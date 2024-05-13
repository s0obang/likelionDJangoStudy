from django.contrib import admin
from django.urls import path, include

from todo.views import todo_list, todo_detail, todo_edit, todo_post, todo_done, todo_done_list, todo_discard


app_name='todo'

urlpatterns = [
    path('', todo_list, name='todo_list' ),
    path('<int:pk>/', todo_detail, name='todo_detail'),
    path('post/', todo_post, name='todo_post'),
    path('<int:pk>/edit/', todo_edit, name='todo_edit'),
    path('done/', todo_done_list, name='todo_done_list'),
    path('done/<int:pk>', todo_done, name='todo_done'),
    path('discard/<int:pk>', todo_discard, name='todo_discard'),
]
                                                                                                                                 
