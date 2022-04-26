from django.db import models


class Comment(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}: {self.title} -- {self.content}'
