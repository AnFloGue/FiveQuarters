from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('shop/', include('frontshop.urls')),
    path('accounts/', include('accounts.urls')),
    path('inventory/', include('inventory.urls')),
]