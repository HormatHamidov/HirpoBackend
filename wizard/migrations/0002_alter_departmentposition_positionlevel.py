# Generated by Django 4.1.7 on 2023-08-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentposition',
            name='positionlevel',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
