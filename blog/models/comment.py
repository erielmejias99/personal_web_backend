from django.db import models
from django.utils import timezone


class BlogComment( models.Model ):
    nickname = models.CharField( max_length = 100, blank = False, null = False )
    email = models.CharField( max_length = 150, blank = False, null = True )
    text = models.TextField( max_length = 500, blank = False, null = False )

    star = models.IntegerField()

    date = models.DateTimeField( default = timezone.now )

    class Meta:
        db_table = 'blog_comment'

    def __str__(self):
        return "nickname: {} | email: {} | date: {}".format( self.nickname, self.email, self.date )