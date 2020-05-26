from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Activity(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    duration = models.CharField(max_length=120)
    job = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=200)


    def __str__(self):
        return self.field.name

    class Meta:
        verbose_name_plural = 'Activities'


