import factory
from learning.models import Resource


class ResourceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Resource