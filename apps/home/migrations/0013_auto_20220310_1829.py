# Generated by Django 3.2.11 on 2022-03-10 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_cachier_orders_payment_methods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cachier',
            name='contact',
            field=models.CharField(default='null', max_length=500),
        ),
        migrations.AlterField(
            model_name='cachier',
            name='first_name',
            field=models.CharField(default='null', max_length=500),
        ),
        migrations.AlterField(
            model_name='cachier',
            name='hidden',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cachier',
            name='img_name',
            field=models.CharField(default='null', max_length=500),
        ),
        migrations.AlterField(
            model_name='cachier',
            name='img_url',
            field=models.CharField(default='null', max_length=500),
        ),
        migrations.AlterField(
            model_name='cachier',
            name='last_name',
            field=models.CharField(default='null', max_length=500),
        ),
        migrations.AlterField(
            model_name='cachier',
            name='password',
            field=models.CharField(default='null', max_length=500),
        ),
        migrations.AlterField(
            model_name='cachier',
            name='user_id',
            field=models.IntegerField(default=1),
        ),
    ]
