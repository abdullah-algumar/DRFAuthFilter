from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static


from rest.views import KurulusViewSet, LoginView, RegisterView, SubscribeViewSet, KurulusListView

router = DefaultRouter()
router.register(r'kurulus', KurulusViewSet)
router.register(r'takip', SubscribeViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="API Dokümantasyonu",
        default_version='v1',
        description='''Bu Api : 
        - Authentication (register ve login).
        - Kurulus model uzerinde CRUD yapmak ve kuruluslarin filterlemesi
        - Takip edip takiplerin listelemesi.
          yapan bir DRF Api. ''',
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # auth urls
    path('auth/register/', RegisterView.as_view(), name='register-api'),
    path('auth/login/', LoginView.as_view(), name='login-api'),

    # rest urls
    path('rest/', include(router.urls)),
    path('rest/kuruluslist', KurulusListView.as_view()),

    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)