from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='Blogs')
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    img = models.ImageField( upload_to = 'blog_img', null=False, blank=False, width_field=500, height_field=500)

    class Meta:
        db_table = 'blog'

    def __str__(self):
        return "owner: {} | title: {}".format( self.owner, self.title )