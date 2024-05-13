from django.urls import path
from .views import guestbook, write, delete, deleteform


app_name='guestbook'

urlpatterns = [
    path('', guestbook, name='guestbook'),
    path('write/', write, name='write'),
    path('delete/', delete, name='delete'),
    path('deleteform/<int:id>', deleteform, name='deleteform'),
]