# Generated by Django 3.2.7 on 2021-10-15 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoEcommerce', '0003_auto_20211015_1506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='cat_title',
            new_name='cat_id',
        ),
    ]