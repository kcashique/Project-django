# Generated by Django 4.0.2 on 2022-03-10 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_product_options_rename_name_product_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]