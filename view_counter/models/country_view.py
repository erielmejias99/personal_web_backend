from django.db import models


class CountryView( models.Model ):

    country = models.CharField( max_length = 250, null = False, blank = False )
    count = models.PositiveBigIntegerField( null=False, blank=False, default = 1 )

    class Meta:
        db_table = 'country_view'

    def __str__(self):
        return "country: {} | count: {}".format( self.country, self.count )