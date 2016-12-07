from django.db import models


class API_log(models.Model):
    remote_addr = models.CharField(max_length=100)
    submit_date = models.DateTimeField()
    success = models.BooleanField(default=False)

    class META:
        ordering = ['-submit_date']

    def __str__(self):
        return str(self.submit_date)
