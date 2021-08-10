from rest_framework import routers
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from leads.api.viewset import LeadViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="TESTE Laborit cadastro de Email API",
        default_version='v1',
        description="Documentacao APIS",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.SimpleRouter()
router.register(r'api/v1/email', LeadViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
admin.site.site_header = "Laborit"

admin.site.index_title = "Laborit"

admin.site.site_title = "Laobrit"
