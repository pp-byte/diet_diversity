# Generated by Django 3.1.5 on 2021-08-30 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20210830_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='Consistency',
            field=models.CharField(blank=True, default='thick', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='Recipe_List',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
    ]
