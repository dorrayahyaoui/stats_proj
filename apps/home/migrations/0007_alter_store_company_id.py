# Generated by Django 3.2.11 on 2022-03-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_s2c_id_store_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='company_id',
            field=models.IntegerField(null=True),
        ),
    ]