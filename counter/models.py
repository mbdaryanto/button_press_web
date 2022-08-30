from django.db import models
from django.contrib.auth.models import User


class UserPress(models.Model):
    """
    to store the time a user press to increment
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    at = models.DateTimeField()

    class Meta:
        indexes = [
            models.Index(fields=['user', 'at'])
        ]


    def __str__(self):
        return "{} {}".format(self.user.get_username(), self.at)


class PressCounter(models.Model):
    """
    to store the global button press counter
    """
    number = models.IntegerField()
    _singleton = models.BooleanField(default=True, editable=False, unique=True)

    def __str__(self):
        return "{}".format(self.number)
