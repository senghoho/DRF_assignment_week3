# Generated by Django 4.2.3 on 2023-07-31 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='num',
            new_name='like',
        ),
    ]
