# Generated by Django 2.2.19 on 2021-02-27 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Indikator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField(max_length=500, null=True)),
                ('angka_kredit', models.IntegerField(default=0, null=True)),
                ('kuantitas', models.IntegerField(default=1, null=True)),
                ('kualitas', models.IntegerField(default=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Indikator Kegiatan',
            },
        ),
        migrations.CreateModel(
            name='Jabatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Jabatan',
            },
        ),
        migrations.CreateModel(
            name='Pegawai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nip', models.CharField(max_length=18, null=True)),
                ('nama', models.CharField(max_length=100, null=True)),
                ('pangkat', models.CharField(max_length=100, null=True)),
                ('golrung', models.CharField(max_length=5, null=True)),
                ('jabatan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kinerja.Jabatan')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Pegawai',
            },
        ),
        migrations.CreateModel(
            name='Satuan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Satuan',
            },
        ),
        migrations.CreateModel(
            name='Sasaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField(max_length=500, null=True)),
                ('tahun', models.CharField(max_length=4, null=True)),
                ('pegawai', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kinerja.Pegawai')),
            ],
            options={
                'verbose_name_plural': 'Sasaran Kegiatan',
            },
        ),
        migrations.CreateModel(
            name='Realisasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bulan', models.CharField(max_length=20, null=True)),
                ('kuantitas', models.IntegerField(default=1, null=True)),
                ('kualitas', models.IntegerField(default=0, null=True)),
                ('indikator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kinerja.Indikator')),
            ],
            options={
                'verbose_name_plural': 'Realisasi Indikator',
            },
        ),
        migrations.CreateModel(
            name='PejabatPenilai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atasan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atasan', to='kinerja.Pegawai')),
                ('pegawai', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pegawai', to='kinerja.Pegawai')),
            ],
            options={
                'verbose_name_plural': 'Pejabat Penilai',
            },
        ),
        migrations.AddField(
            model_name='indikator',
            name='sasaran',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kinerja.Sasaran'),
        ),
        migrations.AddField(
            model_name='indikator',
            name='satuan',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kinerja.Satuan'),
        ),
    ]
