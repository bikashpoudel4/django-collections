from django.contrib import admin
from .models import Summernote

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    
admin.site.register(Summernote, PostAdmin)

