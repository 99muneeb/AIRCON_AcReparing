# Generated by Django 4.0.2 on 2022-04-10 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
