from email.policy import default
from django.db import models

# Create your models here.
class GamePost(models.Model):
    n = models.PositiveIntegerField(null=True, blank=True)
    bitstring = models.TextField(default="")
    Pi = []

    # for i in range(2, int(n)+1):
    #     choice = []
    #     for c in range(1, i):
    #         choice.append(f"{c}")
    #     choice.append("all")

    #     Pi.append(models.CharField(
    #         max_length = 100,
    #         choices = choice,
    #         default = '1'
    #     ))
