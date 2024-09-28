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
        title="fivequarters API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# ==============================
# Admin View
# ==============================
urlpatterns = [
    path('admin/', admin.site.urls),

    # ==============================
    # API Endpoints, for version 1
    # ==============================
    path('api/v1/', include('api.urls_v1')),

    # ==============================
    # Inventory App
    # ==============================
    path('inventory/', include('inventory.urls')),
    
    # ==============================
    # Frontshop App
    # ==============================
    path('frontshop/', include('frontshop.urls')),
    
    # ==============================
    # Swagger and Redoc Documentation
    # ==============================
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Serve static files in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)