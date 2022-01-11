# Generated by Django 3.2.5 on 2022-01-04 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_quest_text_question_question_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_title', models.CharField(max_length=30)),
                ('b_writter', models.CharField(max_length=15)),
                ('b_maintext', models.CharField(max_length=200)),
                ('b_date', models.DateTimeField(auto_now=True)),
                ('b_like_count', models.IntegerField(default=0)),
                ('b_comment_count', models.IntegerField(default=0)),
            ],
        ),
    ]