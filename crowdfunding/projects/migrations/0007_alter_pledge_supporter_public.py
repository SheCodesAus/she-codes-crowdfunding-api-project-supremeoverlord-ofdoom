# Generated by Django 4.1.5 on 2023-01-29 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_remove_project_liked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='supporter_public',
            field=models.CharField(max_length=200),
        ),
    ]