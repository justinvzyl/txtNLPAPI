# Generated by Django 2.2.1 on 2019-05-16 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_backlogcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='backlogcomment',
            name='owner',
            field=models.CharField(blank=True, default='None', max_length=254),
        ),
    ]