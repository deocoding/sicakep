from django.contrib import admin
from .models import *


@admin.register(Jabatan)
class JabatanAdmin(admin.ModelAdmin):
    list_display = ("nama", )
    search_fields = ["nama",]

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     form.base_fields["nama"].label = "Jabatan"
    #     return form


@admin.register(Pegawai)
class PegawaiAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user', 'jabatan']
    list_display = ("nama", "nip", "jabatan")
    search_fields = (["nama", "nip", "jabatan__nama"])


@admin.register(PejabatPenilai)
class PejabatPenilaiAdmin(admin.ModelAdmin):
    autocomplete_fields = ['atasan', 'pegawai']
    list_display = ("atasan", "pegawai")    
    search_fields = (["atasan__nama", "pegawai__nama"])


@admin.register(Sasaran)
class SasaranAdmin(admin.ModelAdmin):
    # autocomplete_fields = ['pegawai']
    list_display = ("nama", )    
    search_fields = (["nama", ])


@admin.register(Satuan)
class SatuanAdmin(admin.ModelAdmin):
    list_display = ("nama", )
    search_fields = ["nama",]


@admin.register(Indikator)
class IndikatorAdmin(admin.ModelAdmin):
    autocomplete_fields = ['sasaran', ]
    list_display = ("sasaran", "nama")    
    search_fields = (["sasaran__nama", "nama", ])

admin.site.register(BulanPenyelesaian)

@admin.register(Kegiatan)
class KegiatanAdmin(admin.ModelAdmin):
    autocomplete_fields = ['pegawai', 'indikator', 'satuan', ]
    list_display = ("pegawai", "indikator", "kegiatan")    
    search_fields = (["pegawai__nama", "indikator__nama", "kegiatan"])

