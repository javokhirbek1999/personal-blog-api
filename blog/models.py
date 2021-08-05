from django.db import models
from django.contrib.auth import get_user_model

from ckeditor.fields import RichTextField



def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    
class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    
    status_options = (
        ('published','published'),
        ('draft','draft'),
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    thumbnail = models.ImageField(upload_to=upload_to, default='posts/default.jpg')
    content = RichTextField()
    slug = models.SlugField(max_length=200, unique_for_date='published')
    published = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    status = models.CharField(max_length=200, choices=status_options, default='draft')
    objects = models.Manager()
    postobjects = PostObjects()

    class Meta:
        ordering = ('-published',)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-posted',)

    def __str__(self):
        return self.post.title
    

class Reply(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('-posted',)
    
    def __str__(self):
        return self.comment.body

def allComments(post):
    return Comment.objects.filter(post__slug=post.slug)

def allReplies(comment):
    return Reply.objects.filter(comment_id=comment.id)