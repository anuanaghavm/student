from django.db import models

class Students(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    mobile=models.IntegerField()

    def __str__(self):
        return self.first_name