# Generated by Django 3.2.11 on 2022-03-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20220310_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cachier',
            name='contact',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cachier',
            name='first_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cachier',
            name='img_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cachier',
            name='img_url',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cachier',
            name='last_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cachier',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]
