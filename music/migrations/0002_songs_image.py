# Generated by Django 2.1.2 on 2018-10-29 04:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='image',
            field=models.FileField(default=django.utils.timezone.now, max_length=1000, upload_to=''),
            preserve_default=False,
        ),
    ]