# Generated by Django 4.1.6 on 2023-02-04 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authphone', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authphone',
            name='id',
        ),
        migrations.AlterField(
            model_name='authphone',
            name='phone',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
