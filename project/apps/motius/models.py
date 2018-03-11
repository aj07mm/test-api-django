from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=50, blank=False)
    author = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return u"%s" % self.name

    class Meta:
        permissions = (
            # name
            ('read_name_article', "Read article's name"),
            ('change_name_article', "Change article's name"),

            # author
            ('read_author_article', "Read article's author"),
            ('change_author_article', "Change article's author"),
        )
