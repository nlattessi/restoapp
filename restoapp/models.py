from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=128, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Presentacion(models.Model):
    nombre = models.CharField(max_length=128, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Menu(models.Model):
    nombre = models.CharField(max_length=128, unique=True)
    descripcion = models.TextField()
    precio = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria)
    presentacion = models.ForeignKey(Presentacion)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    menu = models.ManyToManyField(Menu)
    ESTADOS = (
        ('P', 'PEDIDO'),
        ('C', 'COCINA'),
        ('M', 'MOSTRADOR'),
        ('D', 'DELIVERY'),
        ('E', 'ENTREGADO'),
    )
    estado = models.CharField(max_length=1, choices=ESTADOS)
    fechahora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id + " / " + self.fechahora

