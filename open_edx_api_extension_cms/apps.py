from django.apps import AppConfig


class OpenEdxApiExtensionXmsConfig(AppConfig):
    name = 'open_edx_api_extension_cms'
    verbose_name = "Open edX API extension CMS"

    def ready(self):
        import open_edx_api_extension_cms.signals
