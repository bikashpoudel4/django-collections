from django.db import models

class Summernote(models.Model):
    title = models.CharField(max_length=200)
    
    content = models.TextField() # django-summernote fucus this content from admin.py
    
    def __str__(self):
        return f"{self.title}"

