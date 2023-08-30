from rest_framework.routers import DefaultRouter
from rest.views import KurulusViewSet


router = DefaultRouter()
router.register(r'kurulus', KurulusViewSet)