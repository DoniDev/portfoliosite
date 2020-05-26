from django.db import models
from owner.models import Owner


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Greeting(models.Model):
    starting = models.CharField(max_length=200)
    name = models.ForeignKey(Owner, on_delete=models.CASCADE,default='')
    intro = models.CharField(max_length=50, default='')
    skills = models.ManyToManyField(Skill)

    class Meta:
        verbose_name_plural = 'Introduction'

    def __str__(self):
        return f'{self.name.full_name} introduction'





