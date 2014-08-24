from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.nombre


class Grupo(models.Model):
    nombre = models.CharField(max_length=128, unique=True)
    categoria = models.ForeignKey(Categoria)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=128, unique=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    grupo = models.ForeignKey(Grupo)
    descripcion = models.TextField(blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


'''class Pedido(models.Model):
    menu = models.ForeignKey(Menu)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return '{cantidad} {menu}'.format(
            cantidad=self.cantidad,
            menu=self.menu.nombre,
        )

class Compra(models.Model):
    pedido = models.ManyToManyField(Pedido)
    ESTADOS = (
        ('I', 'INICIADO'),
        ('C', 'COCINA'),
        ('M', 'MOSTRADOR'),
        ('D', 'DELIVERY'),
        ('E', 'ENTREGADO'),
    )
    estado = models.CharField(max_length=1, choices=ESTADOS)
    fechahora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{id} {fechahora}'.format(
            id=self.id,
            fechahora=self.fechahora.strftime("%Y-%m-%d %H:%M:%S"),
        )
'''
