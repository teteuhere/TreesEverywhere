# Generated by Django 5.1.4 on 2024-12-10 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantedtree',
            name='planted_at',
            field=models.DateTimeField(),
        ),
    ]