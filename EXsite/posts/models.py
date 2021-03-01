from django.db import models

class Post(models.Model):
    Post_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')