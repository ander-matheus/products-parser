# Generated by Django 5.1.1 on 2024-10-04 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0002_consumerlog_exception_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consumerlog',
            options={'ordering': ['-pk']},
        ),
    ]
