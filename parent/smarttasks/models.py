# Imports
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


# BEGIN

class STask(models.Model):

    sid = models.UUIDField(_("Unique ID for the S Task"), primary_key=True, blank=False, default=uuid4, editable=False)
    name = models.CharField(_("Name for the S Task"), max_length=100, blank=False, unique_for_date=True)
    instructions = models.TextField(_("Instrunctions for the S Task"), blank=False)


    class Meta:
        verbose_name = _("stasks")
        verbose_name_plural = _("stasks")

    def __str__(self):
        return self.name

# END

if __name__ == '__main__':
    pass