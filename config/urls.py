from django.contrib import admin
from django.urls import path, include
import accounts.views
import status.views
from front.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('/', include('front.urls')),
    path('accounts/', include('accounts.urls')),
    path('login/', accounts.views.login),
    path('main/', include('roadmap.urls')),
    path('testapi/', include('testapi.urls')),
    path('status/', include('status.urls')),
]
