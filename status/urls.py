from django.urls import path
from .views import select_data, display_data


urlpatterns = [
   path('', select_data, name="status"),
   path('displaydata', display_data, name="displaydata"),
]