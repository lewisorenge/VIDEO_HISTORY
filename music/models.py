from django.db import models

class music(models.Model):
    Title = models.CharField(max_length=200, null=False)
    link = models.URLField(max_length=200, null=False)

    def __str__(self):
        
        return self.Title

    def get_absolute_url(self):
        return reverse('music', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "Music"
