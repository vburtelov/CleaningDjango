from rest_framework import routers
from api.views import UserViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet, 'user')
router.register('order', OrderViewSet, 'order')

urlpatterns = router.urls
