# Generated by Django 2.2.16 on 2022-04-15 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_auto_20220414_1409'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='review',
            name='title_author',
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='unique_review'),
        ),
    ]