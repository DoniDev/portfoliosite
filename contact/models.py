from django.db import models
from owner.models import Owner


class Contact(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    credentials = models.ForeignKey(Owner, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='contact/', null=True)


    class Meta:
        verbose_name_plural = 'contact'

    def __str__(self):
        return self.credentials.full_name
