from django.db import models


class User(models.Model):
    userId = models.CharField(max_length=100)
    userPw = models.CharField(max_length=100)
    userName = models.CharField(max_length=100)
    userPhone = models.CharField(max_length=20)
    userInfo = models.CharField(max_length=100)
    userPromotion = models.IntegerField()

    def __str__(self):
        return self.userId