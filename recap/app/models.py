from django.db import models

class AppModel(models.Model):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    age = models.IntegerField(null=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"