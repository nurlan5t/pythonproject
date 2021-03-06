import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Lenta(models.Model):
    article_title = models.CharField('Article title', max_length = 100)
    article_text = models.TextField('Article text')
    publication_date = models.DateTimeField('Date of publication')
    def __str__(self):
        return  self.article_title
    def was_published_recently(self):
        return self.publication_date >= (timezone.now() - datetime.timedelta(days = 7))
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
class Comment(models.Model):
    lenta = models.ForeignKey(Lenta, on_delete = models.CASCADE)
    author_name = models.CharField('Author_name', max_length = 50)
    comment_text = models.CharField('Comment_text', max_length = 200)
    def __str__(self):
        return  self.author_name
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Post(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    title = models.CharField('Post title', max_length=150)
    description = models.TextField()
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Post_Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'