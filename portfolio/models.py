from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=80)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='images', default=None)
    text = models.TextField()
    url = models.URLField(default=None)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
