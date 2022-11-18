from django.db import models
from django.urls import reverse

# Create your models here.
class Catelog(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.name

class Articles(models.Model):
    catelog = models.ForeignKey(Catelog, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250)
    title = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='images/')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Article'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('page:detailpage', args=[self.slug])
