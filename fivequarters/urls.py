# fivequarters/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configure the schema view for Swagger and Redoc documentation
schema_view = get_schema_view(
   openapi.Info(
      title="fivequarters API",  # Title of the API documentation
      default_version='v1',  # Default version of the API
      description="API documentation",  # Description of the API
      terms_of_service="https://www.google.com/policies/terms/",  # Terms of service URL
      contact=openapi.Contact(email="contact@yourapi.local"),  # Contact information
      license=openapi.License(name="BSD License"),  # License information
   ),
   public=True,  # Make the documentation public
   permission_classes=(permissions.AllowAny,),  # Allow any permissions to access the documentation
)

# Define the URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL

    # API endpoints
    path('api/v1/', include('api.urls_v1')),  # Include version 1 of the API URLs

    # Inventory app
    path('inventory/', include('inventory.urls')),  # Include URLs for the inventory app

    # Swagger and Redoc documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI documentation
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Redoc UI documentation
]

# Serve static files in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)