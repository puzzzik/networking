from django.urls import path
from .views import list_files
urlpatterns = [
    path('get_files/', list_files)
]