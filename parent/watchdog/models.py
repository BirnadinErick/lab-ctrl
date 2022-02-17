# Imports
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# BEGIN

class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.TextField(
        _("Role of the User"),
        default="Administrator",
        max_length=20,
        blank=False
    )

class Child(models.Model):

    cid = models.UUIDField(_("Unique Child ID"), primary_key=True, default=uuid4, editable=False)
    nickname = models.CharField(_("Nickname"), max_length=50, blank=True)
    ip = models.GenericIPAddressField(_("IP-Addr of the child"), protocol="both", unpack_ipv4=True, blank=False, unique=True)
    isIPStatic = models.BooleanField(_("Is the IP Static or not?"), blank=False)
    nurse_check_interval = models.IntegerField(_("Nurse Check Interval Value"), blank=False)
    nurse_check_type = models.IntegerField(_("Nurse Check Type"), blank=False)
    sidenote = models.TextField(_("Sidenote on the child"), blank=True)
    class Meta:
        verbose_name = _("child")
        verbose_name_plural = _("children")

    def __str__(self):
        return self.ip

class STask_Child(models.Model):

    sid = models.ForeignKey("smarttasks.STask", verbose_name=_("sid of the s task"), on_delete=models.CASCADE)
    cid = models.ForeignKey("watchdog.Child", verbose_name=_("cid of the target child"), on_delete=models.CASCADE)
    cron = models.FloatField(_("Timestamp of the scheduled time"))
    class Meta:
        verbose_name = _("STask and child")
        verbose_name_plural = _("STasks and Children")

    def __str__(self):
        return f"{self.sid} on {self.cid}"

    
# END

if __name__ == '__main__':
    pass