from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('Date Published')
    content = models.TextField()
    slug = models.SlugField()
    link = models.URLField(blank=True)

    def __unicode__(self):
        return self.title
