# Generated by Django 2.2.14 on 2020-07-25 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth0login', '0003_eventlog_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='raw_text',
            field=models.TextField(),
        ),
    ]