from django.contrib import admin
from .models import *

# admin.site.register(Jabatan)
@admin.register(Jabatan)
class JabatanAdmin(admin.ModelAdmin):
    list_display = ("nama", )
    search_fields = ["nama",]

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     form.base_fields["nama"].label = "Jabatan"
    #     return form

# admin.site.register(Pegawai)
@admin.register(Pegawai)
class PegawaiAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user', 'jabatan']
    list_display = ("nama", "nip", "jabatan")
    search_fields = (["nama", "nip", "jabatan__nama"])

# admin.site.register(PejabatPenilai)
@admin.register(PejabatPenilai)
class PejabatPenilaiAdmin(admin.ModelAdmin):
    autocomplete_fields = ['atasan', 'pegawai']
    list_display = ("atasan", "pegawai")    
    search_fields = (["atasan__nama", "pegawai__nama"])

# admin.site.register(Sasaran)
@admin.register(Sasaran)
class SasaranAdmin(admin.ModelAdmin):
    autocomplete_fields = ['pegawai']
    list_display = ("nama", "pegawai")    
    search_fields = (["nama", "pegawai__nama"])

# admin.site.register(Satuan)
@admin.register(Satuan)
class SatuanAdmin(admin.ModelAdmin):
    list_display = ("nama", )
    search_fields = ["nama",]

# admin.site.register(Indikator)
@admin.register(Indikator)
class IndikatorAdmin(admin.ModelAdmin):
    autocomplete_fields = ['sasaran', 'satuan']
    list_display = ("sasaran", "nama")    
    search_fields = (["sasaran__nama", "nama", ])

admin.site.register(BulanPenyelesaian)
admin.site.register(Realisasi)
