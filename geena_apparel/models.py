from django.db import models


class UserCounter(models.Model):
    ip_address = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'User Counter'

    def __str__(self):
        return self.ip_address
