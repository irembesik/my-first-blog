# Generated by Django 3.2.21 on 2023-10-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
