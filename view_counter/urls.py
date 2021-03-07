from django.urls import path
from rest_framework.routers import DefaultRouter

from view_counter.views import CountryViewSet, total_site_views

router = DefaultRouter()

router.register( 'country_view', CountryViewSet )

urlpatterns = [
    path( 'total_view/', total_site_views  )
] + router.urls