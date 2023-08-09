from django.db import models

class Repository(models.Model):
    name = models.CharField(max_length=200)
    github_username = models.CharField(max_length=100)
    github_external_id = models.PositiveIntegerField()
    url = models.URLField()
    stars = models.PositiveIntegerField()

    def __str__(self):
        return self.name
