from django.db import models

# Create your models here.


class Blogger(models.Model):
    blogger_id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    profile_picture = models.ImageField(upload_to='bloggers_profiles/',
                                         default='bloggers_profiles/default.avif')
    password = models.CharField(max_length=3000,editable=False)

    def __str__(self):
        return f'Blogger ID: {self.blogger_id}, First Name: {self.first_name}, Last Name: {self.last_name}'


class Blog(models.Model):

    CATEGORY_CHOICES = [
        ('Weight Loss', 'Weight Loss'),
        ('Weight Gain', 'Weight Gain'),
        ('Food', 'Food'),
        ('Health', 'Health'),
        ('Yoga', 'Yoga'),
        ('Muscle Gain', 'Muscle Gain'),
    ]

    blog_id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=3000)
    category = models.CharField(max_length=300,choices=CATEGORY_CHOICES)
    introduction = models.TextField(max_length=6000)
    sub_heading1 = models.CharField(max_length=1000)
    content1 = models.TextField(max_length=10000)
    sub_heading2 = models.CharField(max_length=1000)
    content2 = models.TextField(max_length=10000)
    sub_heading3 = models.CharField(max_length=1000)
    content3 = models.TextField(max_length=10000)
    sub_heading4 = models.CharField(max_length=1000)
    content4 = models.TextField(max_length=10000)
    post_date = models.DateTimeField(auto_now=True)
    published_by = models.ForeignKey(Blogger,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'Blog ID: {self.blog_id}, category: {self.category}'

