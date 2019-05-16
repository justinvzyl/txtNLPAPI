# Generated by Django 2.2.1 on 2019-05-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190516_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackLogComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('topic', models.CharField(default='None', max_length=254)),
                ('comment', models.TextField()),
                ('polarity', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=6)),
                ('subjectivity', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=6)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
