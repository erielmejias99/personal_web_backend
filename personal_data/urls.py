from rest_framework.routers import DefaultRouter

from personal_data.views import PersonalDataViewSet

router = DefaultRouter()

router.register( 'personal_data', PersonalDataViewSet )

urlpatterns = router.urls