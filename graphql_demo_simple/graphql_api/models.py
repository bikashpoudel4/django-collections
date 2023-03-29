from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=250)
    # where folowers can have ManyToManyField relation
    # followers are also the users
    # so from app's ('graphql_api.User') class User
    followers = models.ManyToManyField('graphql_api.User')