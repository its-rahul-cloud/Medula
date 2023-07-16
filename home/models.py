from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *
from .text_to_audio import *
from autoslug import AutoSlugField



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='Profileimage',default='Profileimage/defaul.jpg',null=True)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)



class Category(models.Model):


    name = models.CharField(max_length=100, unique=True)
    image=models.ImageField(upload_to='Categories',null=True,blank=True)
    slug = AutoSlugField(populate_from="name", unique=True)

    def __str__(self):
        return self.name

class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = AutoSlugField(populate_from="title", unique=True,default='CSE')
    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='blog')
    audio =models.FileField(upload_to = 'audio',null= True , blank= True)
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
   # comment = models.ForeignKey(Comment, blank=True, null=True )


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)


    


'''
class Comments(models.Model):

    Profile = models.ForeignKey(Profile, blank=True, null=True,
                             on_delete=models.CASCADE )
    content =  FroalaField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Comment, self).save(*args, **kwargs)
        '''