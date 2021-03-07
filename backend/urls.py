
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh, token_verify

urlpatterns = [

    path( '', TemplateView.as_view( http_method_names=['get'], extra_context={}, template_name='site/index.html')  ),
    path( 'myadmin/', TemplateView.as_view( http_method_names=['get'], extra_context={}, template_name='admin/index.html')  ),
    path( 'admin/', admin.site.urls),

    path('api/token/', token_obtain_pair),
    path('api/token/refresh/', token_refresh),
    path('api/token/verify/', token_verify),

    path( 'api/', include( 'status.urls' ) ),
    path( 'api/', include( 'personal_data.urls' ) ),
    path( 'api/', include( 'skill.urls') ),
    path( 'api/', include( 'experience.urls' ) ),
    path( 'api/', include( 'formation.urls' ) ),
    path( 'api/', include( 'file.urls' ) ),
    path( 'api/', include( 'personal_data.urls' ) )
]
