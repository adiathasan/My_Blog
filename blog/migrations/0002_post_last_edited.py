# Generated by Django 3.0.5 on 2020-04-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_edited',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
