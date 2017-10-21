import json
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient
from django.test import TestCase
from ..models import Resource
from ..serializers import ResourceSerializer
from .factories.resource import ResourceFactory

# Initialize the APIClient app
client = APIClient()


class GetAllResourcesTest(TestCase):
    """ Test modules to GET all resources API """

    def setUp(self):
        ResourceFactory.create_batch(20)

    def test_get_all_resources(self):
        # get API response
        response = client.get('/resources/')
        # get data from DB
        resources = Resource.objects.all()
        serializer = ResourceSerializer(resources, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAResourceTest(TestCase):
    """ Test GET a single resource """

    def setUp(self):
        self.resource = ResourceFactory(id=1)

    def test_get_existing_resource(self):
        response = client.get('/resources/1/')
        serializer = ResourceSerializer(self.resource)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_non_existing_resource(self):
        response = client.get('/resources/2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateAResourceTest(TestCase):
    """ Test Create a single resource"""

    def setUp(self):
        self.valid_payload = {
            'name': 'Hello World Javascript',
            'added': '12/07/1989',
            'url': 'http://www.helloworld.com',
            'short_description': 'Learn how to print hello world in javascript',
            'tags': 'javascript webdevelopment'
        }

        self.invalid_payload = {
            'name': 'Hello World Bananas',
            'added': '',
            'url': 'www.helloworld.com',
            'short_description': 'Learn how to print hello world in javascript',
            'tags': 'javascript '
        }

    def test_create_valid_resource(self):
        response = client.post('/resources/', self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_resource(self):
        response = client.post('/resources/', self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteAResourceTest(TestCase):
    """ Test Delete a resource """
    def setUp(self):
        self.resource = ResourceFactory()

    def test_delete_existent_resource(self):
        response = client.delete('/resources/{}/'.format(self.resource.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_resource(self):
        response = client.delete('/resources/30/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UpdateAResourceTest(TestCase):
    """ Test Update a resource """

    def setUp(self):
        self.valid_payload = {
            'name': 'Hello World Javascript',
            'added': '12/07/1989',
            'url': 'http://www.helloworld.com',
            'short_description': 'Learn how to print hello world in javascript',
            'tags': 'javascript webdevelopment'
        }

        self.invalid_payload = {
            'name': 'Hello World Bananas',
            'added': '',
            'url': 'www.helloworld.com',
            'short_description': 'Learn how to print hello world in javascript',
            'tags': 'javascript '
        }
        self.resource = ResourceFactory()

    def test_update_valid_resource(self):
        response = client.put('/resources/{}/'.format(self.resource.pk), self.valid_payload, format='json')
        self.resource.refresh_from_db()
        self.assertEqual(response.data, ResourceSerializer(self.resource).data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_resource(self):
        response = client.put('/resources/{}/'.format(self.resource.pk), self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)