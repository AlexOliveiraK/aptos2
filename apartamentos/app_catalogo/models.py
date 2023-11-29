from django.db import models

# Create your models here.
class Apartamentos(models.Model):
    id_apto = models.AutoField(primary_key=True)
    numero_apto = models.IntegerField()
    morador = models.TextField(max_length=255)
