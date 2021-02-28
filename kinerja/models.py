from typing import ClassVar
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model


class Jabatan(models.Model):
    nama = models.TextField(verbose_name='Nama Jabatan', max_length=100, null=True, unique=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = '       Jabatan'


class Pegawai(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nama = models.CharField(verbose_name='Nama Pegawai', max_length=100, null=True)
    nip = models.CharField(verbose_name='NIP', max_length=21, null=True)
    pangkat = models.CharField(max_length=100, null=True)
    golrung = models.CharField(verbose_name='Golongan(Ruang)', max_length=5, null=True)
    jabatan = models.ForeignKey(Jabatan, null=True, blank=True, on_delete=models.SET_NULL)
    # jabnil = 

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = '      Pegawai'


class PejabatPenilai(models.Model):
    atasan = models.ForeignKey(Pegawai, null=True, on_delete=models.SET_NULL, related_name='atasan', verbose_name='Pejabat Penilai')
    pegawai = models.ForeignKey(Pegawai, null=True, on_delete=models.SET_NULL, related_name='pegawai', verbose_name='Pegawai Yang Dinilai')

    def __str__(self):
        return self.atasan.nama

    class Meta:
        verbose_name_plural = '     Pejabat Penilai'


class Sasaran(models.Model):
    nama = models.TextField(verbose_name='Sasaran Kegiatan', max_length=500, null=True)
    tahun = models.CharField(max_length=4, null=True)
    pegawai = models.ForeignKey(Pegawai, null=True, on_delete=models.CASCADE, verbose_name='Nama Pegawai')

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = '    Sasaran Kegiatan'


class Satuan(models.Model):
    nama = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = '   Satuan'

class BulanPenyelesaian(models.Model):
    nama = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = '  Bulan'

class Indikator(models.Model):
    BULAN = (
        ('Januari', 'Januari'),
        ('Februari', 'Februari'),
        ('Maret', 'Maret'),
        ('April', 'April'),
        ('Mei', 'Mei'),
        ('Juni', 'Juni'),
        ('Juli', 'Juli'),
        ('Agustus', 'Agustus'),
        ('September', 'September'),
        ('Oktober', 'Oktober'),
        ('November', 'November'),
        ('Desember', 'Desember'),
    )
    sasaran = models.ForeignKey(Sasaran, null=True, on_delete=models.CASCADE, verbose_name='Sasaran Kegiatan')
    nama = models.TextField('Indikator Kinerja', max_length=500, null=True)
    target_mutu = models.IntegerField(null=True, default=100, verbose_name='Target Mutu')
    target_kuantitas = models.IntegerField(null=True, default=1)
    satuan = models.ForeignKey(Satuan, null=True, on_delete=models.SET_NULL)
    waktu_penyelesaian = models.ManyToManyField(BulanPenyelesaian)
    pagu_anggaran = models.DecimalField(decimal_places=2, max_digits=15, null=True, blank=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = ' Indikator Kinerja'


class Realisasi(models.Model):
    bulan = models.CharField(max_length=20, null=True)
    indikator = models.ForeignKey(Indikator, null=True, on_delete=models.CASCADE)
    kuantitas = models.IntegerField(null=True, default=1)
    kualitas = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.indikator.nama

    class Meta:
        verbose_name_plural = 'Realisasi Indikator'