# Generated by Django 4.0.6 on 2022-08-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_alter_profile_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='link_resume',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]