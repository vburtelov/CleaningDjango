from rest_framework import routers
from api.views import UserViewSet

router = routers.DefaultRouter()
router.register('api/user', UserViewSet, 'user')


urlpatterns = router.urls
