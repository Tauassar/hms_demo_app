from django.db import models


# Create your models here.
class Departments(models.Model):

    class Meta:
        db_table = 'departments'

    title = models.CharField(max_length=40)
    sub_title = models.CharField(max_length=200)
    link = models.CharField(max_length=40)

    def __str__(self):
        return self.title
