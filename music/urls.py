from rest_framework import routers
from .api import musicViewSet

router = routers.DefaultRouter()
router.register('api/music', musicViewSet, 'music')

urlpatterns = router.urls