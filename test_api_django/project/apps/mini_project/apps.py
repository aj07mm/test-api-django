from django.apps import AppConfig


class MiniProjectConfig(AppConfig):
    name = 'project.apps.mini_project'

    def ready(self):
        import project.apps.mini_project.signals
