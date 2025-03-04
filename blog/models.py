from email.headerregistry import ContentTransferEncodingHeader
from operator import index
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Author(models.Model):
    first_name = models.CharField(default="None", max_length=50)
    last_name = models.CharField(default="None", max_length=50)
    email = models.EmailField(default='None',max_length=254)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Tag(models.Model):
    caption = models.CharField(max_length=20)


    def __str__(self):
        return self.caption

class Post(models.Model):
    author = models.ForeignKey(Author,on_delete=models.PROTECT,null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts',null=True)
    title = models.CharField(max_length=80)
    excerpt = models.TextField(default='null')
    date = models.DateField(auto_now=True)
    content = models.TextField()
    image = models.ImageField()
    slug = models.SlugField (blank=True)
    tags = models.ManyToManyField(Tag, related_name='posts')
    def __str__(self):
        return f"{self.title} at {self.date}"

    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.author_name} on {self.post.title}'

    class Meta:
        ordering = ['-created_at']



