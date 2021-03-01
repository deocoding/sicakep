from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Pegawai

def profil_pegawai(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name="pegawai")
        instance.groups.add(group)

        Pegawai.objects.create(
            user=instance,
            nama=instance.username
        )

post_save.connect(profil_pegawai, sender=User)