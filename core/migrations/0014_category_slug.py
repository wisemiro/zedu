# Generated by Django 2.2.6 on 2019-10-25 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='slugcat', unique=True),
            preserve_default=False,
        ),
    ]
