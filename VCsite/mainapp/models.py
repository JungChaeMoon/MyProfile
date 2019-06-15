from django.db import models
from datetime import datetime
# Create your models here.


class Comment(models.Model):

    comment_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published',default=datetime.now())

    def __str__(self):
        return self.comment_text