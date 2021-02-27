from django.db import models
from django.contrib.auth.models import User


class Jabatan(models.Model):
    nama = models.TextField(max_length=100,  null=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = '      Jabatan'


class Pegawai(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nip = models.CharField(max_length=18, null=True)
    nama = models.CharField(max_length=100, null=True)
    pangkat = models.CharField(max_length=100, null=True)
    golrung = models.CharField(max_length=5, null=True)
    jabatan = models.ForeignKey(Jabatan, null=True, blank=True, on_delete=models.SET_NULL)
    # jabnil = 

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = '     Pegawai'


class PejabatPenilai(models.Model):
    pegawai = models.ForeignKey(Pegawai, null=True, on_delete=models.SET_NULL, related_name='pegawai')
    atasan = models.ForeignKey(Pegawai, null=True, on_delete=models.SET_NULL, related_name='atasan')

    def __str__(self):
        return self.atasan.nama

    class Meta:
        verbose_name_plural = '    Pejabat Penilai'


class Sasaran(models.Model):
    pegawai = models.ForeignKey(Pegawai, null=True, on_delete=models.CASCADE)
    nama = models.TextField('Sasaran Kegiatan', max_length=500, null=True)
    tahun = models.CharField(max_length=4, null=True)

    def __str__(self):
        return '%s - %s' % (self.pegawai.nama, self.nama)

    class Meta:
        verbose_name_plural = '   Sasaran Kegiatan'


class Satuan(models.Model):
    nama = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = '  Satuan'


class Indikator(models.Model):
    sasaran = models.ForeignKey(Sasaran, null=True, on_delete=models.CASCADE)
    nama = models.TextField(max_length=500, null=True)
    angka_kredit = models.IntegerField(null=True, default=0)
    kuantitas = models.IntegerField(null=True, default=1)
    satuan = models.OneToOneField(Satuan, null=True, on_delete=models.SET_NULL)
    kualitas = models.IntegerField(null=True, default=100)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = ' Indikator Kegiatan'


class Realisasi(models.Model):
    bulan = models.CharField(max_length=20, null=True)
    indikator = models.ForeignKey(Indikator, null=True, on_delete=models.CASCADE)
    kuantitas = models.IntegerField(null=True, default=1)
    kualitas = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.indikator.nama

    class Meta:
        verbose_name_plural = 'Realisasi Indikator'