from django.db import models


# Create your models here.


class freq(models.Model):
    freq_url = models.URLField()
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.freq_url
