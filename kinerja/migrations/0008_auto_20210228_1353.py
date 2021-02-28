# Generated by Django 2.2.19 on 2021-02-28 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kinerja', '0007_auto_20210228_1331'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indikator',
            options={'verbose_name_plural': ' Indikator Kinerja'},
        ),
        migrations.AlterField(
            model_name='indikator',
            name='nama',
            field=models.TextField(max_length=500, null=True, verbose_name='Indikator Kinerja'),
        ),
        migrations.AlterField(
            model_name='indikator',
            name='sasaran',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kinerja.Sasaran', verbose_name='Sasaran Kegiatan'),
        ),
    ]