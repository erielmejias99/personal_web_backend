from rest_framework.routers import DefaultRouter

from skill.views.skill import SkillViewSet

router = DefaultRouter()

router.register( 'skill', SkillViewSet )

urlpatterns = router.urls