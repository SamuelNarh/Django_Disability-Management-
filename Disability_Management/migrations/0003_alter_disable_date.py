# Generated by Django 4.0.8 on 2023-03-14 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disability_Management', '0002_alter_disable_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disable',
            name='date',
            field=models.DateField(),
        ),
    ]
