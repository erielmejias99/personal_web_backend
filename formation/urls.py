from rest_framework.routers import DefaultRouter

from formation.views.formation import FormationViewSet

router = DefaultRouter()

router.register( 'formation', FormationViewSet )

urlpatterns = router.urls