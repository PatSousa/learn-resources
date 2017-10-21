import factory
from learning.models import Resource


class ResourceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Resource

    name = factory.Faker('name')
    added = factory.Faker('date')
    url = factory.Faker('url')
    short_description = factory.Faker('text')
    tags = factory.Faker('words')