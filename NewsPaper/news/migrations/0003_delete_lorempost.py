# Generated by Django 4.2.2 on 2023-07-05 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_lorempost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LoremPost',
        ),
    ]