# Generated by Django 4.1.2 on 2022-10-19 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0008_alter_notebook_ekranboyutu_alter_notebook_fiyat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='diskBoyutu',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='diskTuru',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='ekranBoyutu',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='fiyat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='islemciNesli',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='islemciTipi',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='isletimSistemi',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='marka',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='model',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='modelNo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='puan',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='ram',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='resim',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='urunLink',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='urunSite',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
