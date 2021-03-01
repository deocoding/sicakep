from typing import ClassVar
from django.db import models
from django.contrib.auth.models import User


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
    golrung = models.CharField(verbose_name='Golongan/Ruang', max_length=5, null=True)
    jabatan = models.ForeignKey(Jabatan, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = '      Pegawai'


class Penilai(models.Model):
    nama = models.CharField(verbose_name='Nama Pejabat', max_length=100, null=True)
    nip = models.CharField(verbose_name='NIP', max_length=21, null=True)
    pangkat = models.CharField(max_length=100, null=True)
    golrung = models.CharField(verbose_name='Golongan/Ruang', max_length=5, null=True)
    jabatan = models.ForeignKey(Jabatan, null=True, blank=True, on_delete=models.SET_NULL)
    pegawai = models.ForeignKey(Pegawai, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Pegawai Yang Dinilai')

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = '     Pejabat Penilai'


class Sasaran(models.Model):
    nama = models.TextField(verbose_name='Sasaran Kegiatan', max_length=500, null=True)
    # tahun = models.CharField(max_length=4, null=True)
    # pegawai = models.ForeignKey(Pegawai, null=True, on_delete=models.CASCADE, verbose_name='Nama Pegawai')

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
    nama = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = '  Bulan'


class Indikator(models.Model):
    sasaran = models.ForeignKey(Sasaran, null=True, on_delete=models.CASCADE, verbose_name='Sasaran Kegiatan')
    nama = models.TextField('Indikator Kinerja', max_length=500, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = ' Indikator Kinerja'


class TargetKegiatan(models.Model):
    pegawai = models.ForeignKey(Pegawai, null=True, on_delete=models.CASCADE, verbose_name='Nama Pegawai')
    # bulan = models.OneToOneField(BulanPenyelesaian, null=True, on_delete=models.CASCADE, verbose_name='Bulan')
    indikator = models.ForeignKey(Indikator, null=True, on_delete=models.CASCADE, verbose_name='Indikator Kegiatan')
    kegiatan = models.TextField('Kegiatan Tugas Jabatan', max_length=500, null=True)
    target_kuantitas = models.IntegerField(null=True, default=1, verbose_name='Target Kuantitas')
    satuan = models.ForeignKey(Satuan, null=True, on_delete=models.SET_NULL)
    target_mutu = models.IntegerField(null=True, default=100, verbose_name='Target Mutu')
    # realisasi_kuantitas = models.IntegerField(null=True, default=1, verbose_name='Realisasi Kuantitas')
    # realisasi_mutu = models.IntegerField(null=True, default=0, verbose_name='Realisasi Mutu')

    def __str__(self):
        return self.kegiatan

    # def nilai(self):
    #     nilai = (self.target_mutu + self.realisasi_mutu) / 2
    #     return nilai

    class Meta:
        verbose_name_plural = 'Kegiatan'
        unique_together = ('pegawai', 'indikator', 'kegiatan', )

class RealisasiKegiatan(models.Model):
    target = models.ForeignKey(TargetKegiatan, null=True, on_delete=models.CASCADE, verbose_name='Target Kegiatan')
    realisasi_kuantitas = models.IntegerField(null=True, default=1, verbose_name='Realisasi Kuantitas')
    realisasi_mutu = models.IntegerField(null=True, default=100, verbose_name='Realisasi Mutu')
    bulan = models.ForeignKey(BulanPenyelesaian, null=True, on_delete=models.CASCADE, verbose_name='Realisasi Bulan')
    # realisasi_kuantitas = models.IntegerField(null=True, default=1, verbose_name='Realisasi Kuantitas')
    # realisasi_mutu = models.IntegerField(null=True, default=0, verbose_name='Realisasi Mutu')

    def __str__(self):
        return self.target.kegiatan

    # def nilai(self):
    #     nilai = (self.target_mutu + self.realisasi_mutu) / 2
    #     return nilai

    class Meta:
        verbose_name_plural = 'Realisasi'
        unique_together = ('bulan', 'target')

        
