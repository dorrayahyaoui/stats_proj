# Generated by Django 3.2.11 on 2022-03-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20220311_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cachier',
            name='img_name',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
