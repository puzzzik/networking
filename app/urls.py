from django.urls import path
from .views import *

urlpatterns = [
    path('get_file/', get_file),
    path('list_files/', list_files),
    path('post_file/', post_file),
    path('logout/', logout)
]
