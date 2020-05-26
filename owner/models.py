from django.db import models

class Owner(models.Model):
    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=17)
    address = models.CharField(max_length=200)
    projects = models.IntegerField()
    images = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'Owner'

    def __str__(self):
        return self.full_name


