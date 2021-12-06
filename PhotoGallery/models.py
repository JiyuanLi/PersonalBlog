from django.db import models


# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=200)

    def __str__(self):
        return self.author_name


class Image(models.Model):
    image_title = models.CharField(max_length=200)
    image_file = models.CharField(max_length=200)
    image_pub_date = models.DateTimeField("Publish Date")
    image_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image_like = models.IntegerField(default=0)
    image_dislike = models.IntegerField(default=0)

    def __str__(self):
        return self.image_title
