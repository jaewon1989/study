# Generated by Django 4.1.6 on 2023-02-04 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authphone', '0002_remove_authphone_id_alter_authphone_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authphone',
            name='phone',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]