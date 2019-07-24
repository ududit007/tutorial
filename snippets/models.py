from django.db import models
from django.contrib.auth.models import User


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name='snippets', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['created']