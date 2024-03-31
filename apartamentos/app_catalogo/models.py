from django.db import models

# Create your models here.
class Apartamentos(models.Model):
    id_apto = models.AutoField(primary_key=True)
    numero_apto = models.IntegerField()
    morador = models.CharField(max_length=255)
    aluguel = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.id_apto
