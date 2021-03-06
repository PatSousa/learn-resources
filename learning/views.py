from .models import Resource
from .serializers import ResourceSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Class based views for API. Kept some explicitness
class ResourceList(APIView):
    """
    List all resources for a certain user
    Create a new resource
    """

    def get(self, request):
        resources = Resource.objects.all()
        serializer = ResourceSerializer(resources, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResourceDetail(APIView):
    """
    Get, update or delete a single resource
    """
    @staticmethod
    def get_object(pk):
        try:
            return Resource.objects.get(pk=pk)
        except Resource.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        resource = self.get_object(pk)
        serializer = ResourceSerializer(resource)
        return Response(serializer.data)

    def put(self, request, pk):
        resource = self.get_object(pk)
        serializer = ResourceSerializer(resource, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        resource = self.get_object(pk)
        resource.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



