from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ManyToManyField('Category', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(null=True, blank=True)
    like_count = models.IntegerField(default=0)
    published_date = models.DateTimeField(blank=True, null=True)
    is_anonymous = models.BooleanField(blank=True, null=True, default=False)
    likes = models.ManyToManyField(User, related_name='liked_posts')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    like = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text


class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    posts = models.ManyToManyField('Post', through='PostTag')

    def __str__(self):
        return self.slug


class PostTag(models.Model):
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

