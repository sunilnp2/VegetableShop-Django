# Generated by Django 4.1.1 on 2022-09-17 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_item_dis_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discription',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='dis_price',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.PositiveBigIntegerField(),
        ),
    ]
