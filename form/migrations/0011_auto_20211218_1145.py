# Generated by Django 3.1.5 on 2021-12-18 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0010_auto_20211216_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='unit',
            field=models.CharField(blank=True, default='pieces', max_length=122, null=True),
        ),
    ]
