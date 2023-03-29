from django.db import models

class Category(models.Models):
    name = models.CharField(max_length=255)
    slug = models.slugfield()
    
    class Meta:
        ordering = ('name') #oders by name
        
    def __str__(self):
        return self.name
    
    # This function  is used for url
    # and easier to use in template later
    def get_absolute_url(self):
        return f'/{self.slug/}'