# Generated by Django 2.0.6 on 2018-06-27 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_postcomment_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postcomment',
            options={'ordering': ['created_at']},
        ),
    ]