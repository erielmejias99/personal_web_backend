from django.db import models
from django.utils.timezone import now


class Experience( models.Model ):

    image = models.ImageField( upload_to='experience', null = False, blank = False )

    company = models.CharField( max_length = 250, null = False, blank = False )
    location = models.CharField( max_length = 250, null = True, blank = True )

    occupation = models.CharField(max_length = 30, blank = False, null = False)

    description = models.TextField( max_length = 2000, null = True, blank = True  )
    web_site = models.CharField( max_length=500, null = True, blank = True )

    start_date = models.DateField( default = now, blank = False, null = False )
    end_date = models.DateField( default = now, blank = True, null = True )

    def __str__(self):
        return "company: {} | occupation: {} | location: {} | start_date: {} | end_date: {}"\
            .format(self.company, self.occupation, self.location, self.start_date, self.end_date)

    class Meta:
        db_table = 'experience'