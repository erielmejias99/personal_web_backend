from rest_framework.routers import DefaultRouter

from experience.views.experience import ExperienceViewSet

router = DefaultRouter()

router.register( 'experience', ExperienceViewSet )

urlpatterns = router.urls