# Generated by Django 4.1.2 on 2022-10-26 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]