from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    @property
    def created_format(self):
        return self.created.strftime('%b %d %Y')

    def __str__(self) -> str:
        return self.name
