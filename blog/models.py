from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author  = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """
        diff between redirect and reverse
        redirect returns the url while reverse returns the url as a string
        """
        return reverse('post-detail', kwargs={'pk': self.pk})


class Blog(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    date_posted = models.DateField(null=True)   

