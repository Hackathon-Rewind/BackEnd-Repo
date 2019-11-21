from django.db import models


class Missing(models.Model):
    postId = models.CharField(max_length=100)
    postDate = models.DateTimeField(auto_now=True)
    relation = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    nation = models.CharField(max_length=100)
    missDate = models.CharField(max_length=100)
    missArea = models.CharField(max_length=100)
    physicalPoint = models.CharField(max_length=100)
    additional = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
