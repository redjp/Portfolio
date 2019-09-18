from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    url = models.URLField(default=None)
    thumbnail = models.URLField(default=None)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
