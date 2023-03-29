from django.db import models
import graphene

from graphene_django import DjangoObjectType
from graphql_api import models

# same as serializers
# inheriting from User class DjangoObjectType
class User(DjangoObjectType):
    # to specify Models in graphql
    # we need to specify with meta class
    class Meta:
        model = models.User


class Query(graphene.ObjectType):
    # defining User as a Graphene field
    user = graphene.Field(User, id=graphene.Int())

    def resolve_user(self, info, **kwargs):
        # fetching users by id using get method
        id = kwargs.get("id")

        if id is not None:
            # if theres no id see in models.User's object and get primary key of thet id
            return models.User.objects.get(pk=id)

        return None    

schema = graphene.Schema(query=Query) 