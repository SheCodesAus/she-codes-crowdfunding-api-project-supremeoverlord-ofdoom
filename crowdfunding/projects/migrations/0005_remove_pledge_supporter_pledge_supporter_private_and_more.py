# Generated by Django 4.1.5 on 2023-01-29 02:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0004_project_liked_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pledge',
            name='supporter',
        ),
        migrations.AddField(
            model_name='pledge',
            name='supporter_private',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='supporter_private_pledges', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pledge',
            name='supporter_public',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='supporter_public_pledges', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
