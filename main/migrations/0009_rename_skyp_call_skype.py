# Generated by Django 4.0.6 on 2022-08-15 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_categry_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='call',
            old_name='skyp',
            new_name='skype',
        ),
    ]