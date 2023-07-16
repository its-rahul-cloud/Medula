# Generated by Django 4.2.3 on 2023-07-14 12:57

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_category_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='CSE', editable=False, populate_from='title', unique=True),
        ),
    ]
