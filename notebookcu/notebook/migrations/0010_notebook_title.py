# Generated by Django 4.1.2 on 2022-10-26 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0009_alter_notebook_diskboyutu_alter_notebook_diskturu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
