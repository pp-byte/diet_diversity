# Generated by Django 3.1.5 on 2021-12-16 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0006_auto_20211216_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='recipe_name',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
    ]
