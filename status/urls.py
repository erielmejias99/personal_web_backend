from rest_framework.routers import DefaultRouter

from status.views import StatusViewSet

router = DefaultRouter()

router.register( 'status', StatusViewSet )

urlpatterns = router.urls
