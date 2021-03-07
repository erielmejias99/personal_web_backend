from rest_framework.decorators import api_view
from rest_framework.response import Response

from view_counter.models import CountryView


@api_view( ['GET'] )
def total_site_views( request ):
    total_amount = 0
    for country in CountryView.objects.all():
        total_amount += country.count

    return Response( { 'views': total_amount })