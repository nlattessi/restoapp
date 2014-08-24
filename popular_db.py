import os

def popular():
    #Pizzas
    categoria_pizza = agregar_categoria('Pizza')
    grupo_muzzarella = agregar_grupo('Muzzarella', categoria_pizza)
    agregar_producto('Pizza chica de Muzzarella', 39, grupo_muzzarella)
    agregar_producto('Pizza Grande de Muzzarella', 41, grupo_muzzarella)
    grupo_napolitana = agregar_grupo('Napolitana', categoria_pizza)
    agregar_producto('Pizza chica de Napolitana', 47, grupo_napolitana)
    agregar_producto('Pizza Grande de Napolitana', 52, grupo_napolitana)

    #Empanadas
    categoria_empanada = agregar_categoria('Empanada')
    grupo_jyq = agregar_grupo('Jamon y Queso', categoria_empanada)
    agregar_producto('Empanada de Jamon y Queso', 6, grupo_jyq)
    grupo_carne = agregar_grupo('Carne', categoria_empanada)
    agregar_producto('Empanada de Carne', 6, grupo_carne)

    #Cocina
    categoria_cocina = agregar_categoria('Cocina')
    grupo_platos = agregar_grupo('Plato', categoria_cocina)
    agregar_producto('Albondigas con Pure', 40, grupo_platos)
    agregar_producto('Asado de tira con guarnicion', 68, grupo_platos)
    agregar_producto('Bife de chorizo a la Riojana', 99, grupo_platos)

    #Bebidas
    categoria_bebidas = agregar_categoria('Bebida')
    grupo_gaseosa = agregar_grupo('Gaseosa', categoria_bebidas)
    agregar_producto('Gaseosa 600 cc', 15, grupo_gaseosa)
    agregar_producto('Gaseosa 1 y 1/2 lt', 26, grupo_gaseosa)
    agregar_producto('Gaseosa 2 lt', 28, grupo_gaseosa)
    grupo_cerveza = agregar_grupo('Cerveza', categoria_bebidas)
    agregar_producto('Quilmes lata chica', 18, grupo_cerveza)
    agregar_producto('Quilmes lata de 1/2 lt', 20, grupo_cerveza)
    agregar_producto('Isenbeck descaratable', 30, grupo_cerveza)
    grupo_agua = agregar_grupo('Agua', categoria_bebidas)
    agregar_producto('Agua 1 y 1/2 lt', 22, grupo_agua)

    # Print out what we have added to the user.
    for c in Categoria.objects.all():
        for g in Grupo.objects.filter(categoria=c):
            for p in Producto.objects.filter(grupo=g):
                print( "- {0} - {1} - {2}".format(str(c), str(g), str(p)) )

def agregar_categoria(nombre):
    c = Categoria.objects.get_or_create(nombre=nombre)[0]
    return c

def agregar_grupo(nombre, categoria):
    g = Grupo.objects.get_or_create(nombre=nombre, categoria=categoria)[0]
    return g

def agregar_producto(nombre, precio, grupo, descripcion='', disponible=True):
    p = Producto.objects.get_or_create(nombre=nombre, precio=precio, grupo=grupo, descripcion=descripcion, disponible=disponible)[0]
    return p

# Start execution here!
if __name__ == '__main__':
    print("Ejecutando RestoAPP popular_db.py ...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restoapp_project.settings')
    import django
    django.setup()
    from restoapp.models import Categoria, Grupo, Producto
    popular()
