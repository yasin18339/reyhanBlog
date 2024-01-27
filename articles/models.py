from django.db import models

# Create your models here.
class Article(models.Model):

        title = models.CharField(max_length = 250)
        slug = models.SlugField()
        bady = models.TextField()
        date = models.DateTimeField(auto_now_add = False)
        image = models.ImageField(default='default.jpg',blank=True)

        def __str__(self):
            return self.title

        def snippet(self):
            return self.bady[:250] + ' ...'
