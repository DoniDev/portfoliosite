from django.db import models


class Introduction(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Introduction'


class Service(models.Model):
    icon = models.CharField(max_length=50)
    name = models.CharField(max_length=120)
    heading = models.CharField(max_length=300)

    def __str__(self):
        return self.name


