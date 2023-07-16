from django.contrib import admin

# Register your models here.
from .models import BlogModel, Profile, Category

admin.site.register(BlogModel)
admin.site.register(Profile)
admin.site.register(Category)
