from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=50, blank=False)
    author = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return u"%s" % self.name
