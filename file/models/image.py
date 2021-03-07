from django.db import models


class Image( models.Model ):

    place = models.CharField( max_length = 50, null = False, blank = False )
    image = models.ImageField( null = False, blank = False )

    def __str__(self):
        return "place: {}"\
            .format( self.place )

    class Meta:
        db_table = 'image'