from django.db import models
from django.utils.timezone import now


class Formation( models.Model ):

    image = models.ImageField( null = False, blank = False )

    institution = models.CharField( max_length = 250, null = False, blank = False )

    location = models.CharField( max_length = 250, null = True, blank = True )

    title = models.CharField(max_length = 30, blank = True, null = True )

    web_page = models.CharField( max_length = 500, blank = True, null = True )

    description = models.TextField( max_length = 2000, null = True, blank = True  )

    start_date = models.DateTimeField( default = now, blank = False, null = False )
    end_date = models.DateTimeField( default = None, blank = True, null = True )

    def __str__(self):
        return "institution: {} | location: {} | title: {} | start_date: {} | end_date: {}"\
            .format(self.institution, self.location, self.title, self.start_date, self.end_date)

    class Meta:
        db_table = 'formation'
