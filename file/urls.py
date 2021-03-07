from rest_framework.routers import DefaultRouter

from file.views import ImageViewSet
from file.views.file import FileViewSet

router = DefaultRouter()

router.register( 'image', ImageViewSet )
router.register( 'file', FileViewSet )

urlpatterns = router.urls