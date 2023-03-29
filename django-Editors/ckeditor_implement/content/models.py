from django.db import models

# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Ckeditor(models.Model):
    title = models.CharField(max_length=200)
    
    content = RichTextUploadingField(blank=True) #RichTextUploadingField = for image and file editor
    
    def __str__(self):
        return f"{self.title}"
