# Generated by Django 2.2.7 on 2019-11-21 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20191121_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userPromotion',
            field=models.IntegerField(),
        ),
    ]
