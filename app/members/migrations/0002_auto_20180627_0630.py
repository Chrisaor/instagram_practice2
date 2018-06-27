# Generated by Django 2.0.6 on 2018-06-27 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20180627_0630'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '사용자', 'verbose_name_plural': '사용자 목록'},
        ),
        migrations.AddField(
            model_name='user',
            name='link_posts',
            field=models.ManyToManyField(to='posts.Post', verbose_name='좋아요 누른 포스트 목록'),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(verbose_name='나이'),
        ),
    ]