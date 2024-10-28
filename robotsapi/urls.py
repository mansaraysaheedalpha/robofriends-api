from django.urls import path
from .views import robots_list_serialized

urlpatterns = [
    path('', robots_list_serialized)
]
