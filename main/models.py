from django.db import models

# Create your models here.
class allPosts(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_thumbnail = models.ImageField(upload_to='images/post_img')
    title = models.CharField(max_length=500, default="")
    contents = models.CharField(max_length=10000000, default="")
    author_of_post = models.CharField(max_length=500, default="")
    time = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title