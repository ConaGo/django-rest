# Generated by Django 3.2.9 on 2021-11-09 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snippet',
            options={'ordering': ['created']},
        ),
    ]