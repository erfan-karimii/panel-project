# Generated by Django 4.0.6 on 2022-08-15 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_head_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categry',
            new_name='category',
        ),
    ]
