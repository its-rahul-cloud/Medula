# Generated by Django 4.2.3 on 2023-07-14 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_category_alter_blogmodel_slug_blogmodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Categories'),
        ),
    ]