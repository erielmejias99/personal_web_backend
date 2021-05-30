from django.db import models


class Skill( models.Model ):

    image = models.ImageField( null = False, blank = False )
    label = models.CharField( max_length = 100, null = True, blank = True )
    percent = models.PositiveIntegerField( blank=False, null = True )
    description = models.TextField( max_length = 1500, blank = True, null = True )

    def __str__(self):
        return "label: {}".format( self.label )

    class Meta:
        db_table = 'skill'
