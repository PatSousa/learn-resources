from django.test import TestCase
from .factories.resource import ResourceFactory
from ..models import Resource


class ResourceTest(TestCase):
    """ Test module for Resource model """

    def setUp(self):
        ResourceFactory(name='test123', url='https://myresource.com/aresource')

    def testModelCreate(self):
        self.resource = Resource.objects.get(name='test123')
        self.assertEqual(self.resource.name, 'test123')
        self.assertEqual(self.resource.url, 'https://myresource.com/aresource')
