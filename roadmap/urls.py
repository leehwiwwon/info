from django.urls import path
from .views import get_wms_data

app_name = 'roadmap'
urlpatterns = [
    path('getwms', get_wms_data, name='api'),
]