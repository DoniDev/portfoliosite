from django.db import models

from owner.models import Owner


class About(models.Model):
    starter = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(Owner, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural ='about'

    def __str__(self):
        return f'About {self.user.full_name}'
