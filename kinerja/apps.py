from django.apps import AppConfig


class KinerjaConfig(AppConfig):
    name = 'kinerja'

    def ready(self):
        import kinerja.signals