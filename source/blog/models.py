from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('Date Published')
    description = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(unique=True, max_length=255)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['pub_date']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])
