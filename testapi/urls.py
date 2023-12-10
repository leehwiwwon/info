# yourapp/urls.py
from django.urls import path
from .views import get_wms_data
from .api import get_wms_map
from .api2 import get_wms_legend
urlpatterns = [
    # path('testapi', wms_data_view, name='yourview'),
    # path('getwmsmap', get_wms_map, name='api'),
    path('getwms', get_wms_data, name='api'),
]
