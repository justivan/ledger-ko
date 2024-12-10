from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=120, unique=True)

    def __str__(self) -> str:
        return self.code
