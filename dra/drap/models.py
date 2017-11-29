from django.db import models

# Create your models here.


class Compra(models.Model):

    name = models.CharField(max_length=60)
    cantidad = models.CharField(max_length=60)
    total = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return self.name

    def speak(self):
        return 'The %s says "%s"' % (self.name, self.cantidad)
