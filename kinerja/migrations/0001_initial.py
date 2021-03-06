# Generated by Django 2.2.19 on 2021-03-01 13:20

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
            name='BulanPenyelesaian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': '  Bulan',
            },
        ),
        migrations.CreateModel(
            name='Indikator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField(max_length=500, null=True, verbose_name='Indikator Kinerja')),
            ],
            options={
                'verbose_name_plural': ' Indikator Kinerja',
            },
        ),
        migrations.CreateModel(
            name='Jabatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField(max_length=100, null=True, unique=True, verbose_name='Nama Jabatan')),
            ],
            options={
                'verbose_name_plural': '       Jabatan',
            },
        ),
        migrations.CreateModel(
            name='Pegawai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100, null=True, verbose_name='Nama Pegawai')),
                ('nip', models.CharField(max_length=21, null=True, verbose_name='NIP')),
                ('pangkat', models.CharField(max_length=100, null=True)),
                ('golrung', models.CharField(max_length=5, null=True, verbose_name='Golongan/Ruang')),
                ('jabatan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kinerja.Jabatan')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '      Pegawai',
            },
        ),
        migrations.CreateModel(
            name='Sasaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField(max_length=500, null=True, verbose_name='Sasaran Kegiatan')),
            ],
            options={
                'verbose_name_plural': '    Sasaran Kegiatan',
            },
        ),
        migrations.CreateModel(
            name='Satuan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': '   Satuan',
            },
        ),
        migrations.CreateModel(
            name='TargetKegiatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kegiatan', models.TextField(max_length=500, null=True, verbose_name='Kegiatan Tugas Jabatan')),
                ('target_kuantitas', models.IntegerField(default=1, null=True, verbose_name='Target Kuantitas')),
                ('target_mutu', models.IntegerField(default=100, null=True, verbose_name='Target Mutu')),
                ('indikator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kinerja.Indikator', verbose_name='Indikator Kegiatan')),
                ('pegawai', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kinerja.Pegawai', verbose_name='Nama Pegawai')),
                ('satuan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kinerja.Satuan')),
            ],
            options={
                'verbose_name_plural': 'Kegiatan',
                'unique_together': {('pegawai', 'indikator', 'kegiatan')},
            },
        ),
        migrations.CreateModel(
            name='Penilai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100, null=True, verbose_name='Nama Pejabat')),
                ('nip', models.CharField(max_length=21, null=True, verbose_name='NIP')),
                ('pangkat', models.CharField(max_length=100, null=True)),
                ('golrung', models.CharField(max_length=5, null=True, verbose_name='Golongan/Ruang')),
                ('dinilai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kinerja.Pegawai', verbose_name='Pegawai Yang Dinilai')),
                ('jabatan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kinerja.Jabatan')),
            ],
            options={
                'verbose_name_plural': '     Pejabat Penilai',
            },
        ),
        migrations.AddField(
            model_name='indikator',
            name='sasaran',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kinerja.Sasaran', verbose_name='Sasaran Kegiatan'),
        ),
        migrations.CreateModel(
            name='RealisasiKegiatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realisasi_kuantitas', models.IntegerField(default=1, null=True, verbose_name='Realisasi Kuantitas')),
                ('realisasi_mutu', models.IntegerField(default=100, null=True, verbose_name='Realisasi Mutu')),
                ('bulan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kinerja.BulanPenyelesaian', verbose_name='Realisasi Bulan')),
                ('target', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kinerja.TargetKegiatan', verbose_name='Target Kegiatan')),
            ],
            options={
                'verbose_name_plural': 'Realisasi',
                'unique_together': {('bulan', 'target')},
            },
        ),
    ]
