from django.db import models

# Create your models here.

class reveal(models.Model):
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=10)
    crush=models.CharField(max_length=50)

    def __str__(self):
        return self.code