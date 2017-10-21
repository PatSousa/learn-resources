from django.db import models


# Create your models here.
class Resource(models.Model):
    """
    Resource Model
    Defines the attributes of an added resource
    """
    added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=True, default='')
    url = models.URLField()
    short_description = models.TextField()
    tags = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.name
