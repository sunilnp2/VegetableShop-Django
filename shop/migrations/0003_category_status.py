# Generated by Django 4.1.1 on 2022-09-17 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
