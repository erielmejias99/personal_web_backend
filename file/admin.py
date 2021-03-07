from django.contrib import admin

# Register your models here.
from file.models import File, Image

admin.site.register( Image )
admin.site.register( File )