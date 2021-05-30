from django.db import models


class PersonalData( models.Model ):

    # mdi-icon
    icon = models.CharField( max_length = 100, blank = True, null = True )
    icon_color = models.CharField( max_length = 50, blank = True, null = True )

    label = models.CharField( max_length = 30, blank = True, null = True )

    # data to show
    data = models.CharField( max_length = 1000, blank = False, null = False )
    link = models.CharField( max_length = 250, blank = True, null = True )

    order = models.IntegerField( blank = False, null = False, default = 100 )

    def __str__(self):
        return "icon: {} | ldabel: {} | data: {} | link: {}"

    class Meta:
        db_table = 'personal_data'