from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField('About', max_length=30)
    content = models.TextField('Description')
    tpublish = models.DateTimeField('Date', default=timezone.now)

    def __str__(self):
        return self.title

#    def __unicode__(self):
#       return self.title
