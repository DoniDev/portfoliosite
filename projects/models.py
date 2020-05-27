from django.db import models

class ProjectIntro(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=100)
    technology = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/')
    link = models.URLField()

    def __str__(self):
        return self.name




