# Generated by Django 2.2.3 on 2019-08-17 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Box', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='observationform',
            name='scout',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
