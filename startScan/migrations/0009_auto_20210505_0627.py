# Generated by Django 3.1.6 on 2021-05-05 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0008_auto_20210505_0614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vulnerabilityscan',
            old_name='url',
            new_name='host',
        ),
    ]