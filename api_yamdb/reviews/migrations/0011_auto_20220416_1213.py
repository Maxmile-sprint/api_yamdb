# Generated by Django 2.2.16 on 2022-04-16 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_auto_20220415_1145'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='review',
            name='title_author',
        ),
    ]