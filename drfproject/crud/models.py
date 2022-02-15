from django.db import models

# Create your models here.
class empresa(models.Model):
    name=models.CharField(max_length=50)

class boleto(models.Model):
    name = models.ForeignKey(empresa, on_delete=models.CASCADE, null=False, blank=False)
    code=models.CharField(max_length=50, unique=True)
    valor=models.IntegerField()
    usado=models.BooleanField()