# Generated by Django 4.1.6 on 2023-02-06 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthPhone',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=30, unique=True)),
                ('auth_number', models.IntegerField()),
                ('is_success', models.BooleanField(default=False)),
                ('create_dt', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
