from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings

class SocialPost(models.Model):
    title = models.TextField(max_length=20)
    body = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('socialpost_detail', kwargs={'pk':self.pk})

class Comment(models.Model):
    socialpost = models.ForeignKey(SocialPost, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE,)
    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("article_list")

