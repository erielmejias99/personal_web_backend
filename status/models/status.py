from django.db import models
from django.utils.timezone import now


class Status( models.Model ):
    status = models.CharField( max_length = 250)
    start_date = models.DateField( default = now )
    end_date = models.DateField( null = True, blank = True, default = None )

    def __str__(self):
        return "status: {} | start_date: {} | end_date: {}".format( self.status, self.start_date, self.end_date )

    class Meta:
        db_table = 'status'