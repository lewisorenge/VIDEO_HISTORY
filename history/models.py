from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from .invoke import object_viewed_signal

class history(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True) # returns MUSIC as the type
    object_id = models.PositiveIntegerField() # returns 1, 2, 3, ...
    content_object = GenericForeignKey() # returns actual data
    viewed_on = models.DateTimeField(auto_now_add=True) # returns the time the content was viewed

    def __str__(self):
        
        return "%s viewed on: %s" %s(self.content_object, self.viewed_on)

    class Meta:
        verbose_name_plural = "Histories"

def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    new_history = history.object.create(
        content_type = ContentType.objects.get_for_model(sender),
        object_id = instance.id,
    )

object_viewed_signal.connect(object_viewed_receiver)
