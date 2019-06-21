# Generated by Django 2.2.1 on 2019-06-20 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Box', '0008_auto_20190531_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Box.Player'),
        ),
        migrations.AlterField(
            model_name='player',
            name='agent',
            field=models.TextField(blank=True, null=True),
        ),
    ]
