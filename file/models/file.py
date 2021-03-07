from django.db import models


class File( models.Model ):

    place = models.CharField( max_length = 50, null = False, blank = False )
    file = models.FileField( null = False, blank = False )

    def __str__(self):
        return "place: {}"\
            .format( self.place )

    class Meta:
        db_table = 'file'