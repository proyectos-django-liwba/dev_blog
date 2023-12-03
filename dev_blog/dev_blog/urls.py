
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
# documentación de la API
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
# router de modelos
from categories.api.router import router_categories
from posts.api.router import router_posts
from comments.api.router import router_comments
# para servir archivos de medios en desarrollo
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Dev Blog API",
      default_version='v1',
      description="Documentación de la API Dev Blog",
      terms_of_service="",
      contact=openapi.Contact(email="liwbarqueroh@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('users.api.router')),# solo funciona para APIView
    path('api/', include(router_categories.urls)),
    path('api/', include(router_posts.urls)),
    path('api/', include(router_comments.urls)),
]

# Configuración para servir archivos de medios en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)