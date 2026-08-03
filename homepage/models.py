from django.db import models

# Create your models here.


class HomepageModel(models.Model):
    """Modelo auxiliar para declarar los permisos personalizados de la aplicacion."""

    class Meta:
        managed = False
        default_permissions = ()
        permissions = (
            ('index_viewer', 'Can show to index view (function-based)'),
        )
