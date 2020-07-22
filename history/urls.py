from rest_framework import routers
from .api import historyViewSet

router = routers.DefaultRouter()
router.register('api/history', historyViewSet, 'history')

urlpatterns = router.urls