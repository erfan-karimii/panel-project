# Generated by Django 4.0.4 on 2022-08-15 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('info', '0005_profile_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'مهارت ها', 'verbose_name_plural': 'مهارت ها'},
        ),
        migrations.AlterModelOptions(
            name='circle',
            options={'verbose_name': 'نمودار دایره ای', 'verbose_name_plural': 'نمودار دایره ای'},
        ),
        migrations.AlterModelOptions(
            name='detailprofile',
            options={'verbose_name': 'جزيیات پروفایل', 'verbose_name_plural': 'جزيیات پروفایل'},
        ),
        migrations.AlterModelOptions(
            name='line',
            options={'verbose_name': 'نمودار خطی', 'verbose_name_plural': 'نمودار خطی'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'پروفایل', 'verbose_name_plural': 'پروفایل'},
        ),
        migrations.AddField(
            model_name='profile',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]