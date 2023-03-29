from django.db import models

# Create your models here.
class LaptopModel(models.Model):
    title = models.CharField(max_length=200)
    describe = models.CharField(max_length=300)
    # image = models.ImageField(upload_to="apiDecorater/laptop/")

    def __str__(self):
        return self.title
