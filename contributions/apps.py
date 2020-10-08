from django.apps import AppConfig


class ContributionsConfig(AppConfig):
    name = 'contributions'

    def ready(self):
        import contributions.signals