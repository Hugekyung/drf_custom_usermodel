# Generated by Django 3.2.6 on 2021-08-09 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0005_alter_myuser_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
