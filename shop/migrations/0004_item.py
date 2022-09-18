# Generated by Django 4.1.1 on 2022-09-17 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('dis_price', models.IntegerField()),
                ('image', models.ImageField(upload_to='media/')),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
    ]
