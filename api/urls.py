from rest_framework import routers
from api.views import UserViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register('api/user', UserViewSet, 'user')
router.register('api/order', OrderViewSet, 'order')

urlpatterns = router.urls
