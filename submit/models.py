from django.db import models


class Score(models.Model):
    score = models.IntegerField(default=0)
    username = models.CharField(max_length=100)
    submit_date = models.DateTimeField()

    class Meta:
        ordering = ['-score', 'submit_date', 'username']

    def __str__(self):
        return self.username
