# Generated by Django 3.1.7 on 2021-03-10 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20210310_1244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='desciption',
            new_name='description',
        ),
    ]