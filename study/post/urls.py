from django.urls import path
from .views import write, detail
from django.conf.urls.static import static
from django.conf import settings


app_name='post'

urlpatterns = [
    path('write/', write, name='write'),
    path('<int:id>/', detail, name='detail'),
    
]