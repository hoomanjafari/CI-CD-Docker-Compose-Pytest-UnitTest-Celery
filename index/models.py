from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title', null=True, blank=True)
    caption = models.TextField(verbose_name='Caption')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
