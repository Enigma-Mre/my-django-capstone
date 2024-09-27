from django.db import models

# Create your models here.

class Post(models.Model):

    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 140)
    body = models.TextField(default = 'some string')
    signiture = models.CharField(max_length = 140, default = "Calvin Hattingh")
    date = models.DateTimeField()

    def __str__(self):
        return self.title