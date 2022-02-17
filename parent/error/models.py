# Imports
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


# BEGIN

class Error(models.Model):

    eid = models.UUIDField(_("Unique ID for error"), primary_key=True, default=uuid4, editable=False)
    title = models.CharField(_("Title of the error"), max_length=100, blank=False)
    isHandled = models.BooleanField(_("Isthe error Handled or not?"))
    timestamp = models.FloatField(_("Timestamp of the time the error was recorded"),blank=False, unique=False)
    victim = models.CharField(_("ID of the victim"), max_length=36, blank=True)
    ecode = models.IntegerField(_("Error Code"), blank=False)

    """ NOTE:
        Here, no need to indicate whether the error is due to `child` or `stask`
        as the `ecode` will clarify where this error has occurred
    """
    
    class Meta:
        verbose_name = _("Error")
        verbose_name_plural = _("Errors")

    def __str__(self):
        return self.title


# END

if __name__ == '__main__':
    pass