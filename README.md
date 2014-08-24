v4

Versiones:
python 3.4
django 1.7c3

Comandos:
VirtualEnv:
  workon restoapp
Git:
  git add .
  git commit -am "<mensaje>"
  git push origin master
SQL:
  python manage.py validate
  python manage.py makemigrations restoapp
  python manage.py migrate
ADMIN:
  python manage.py createsuperuser
Server:
  python manage.py runserver 0.0.0.0:8000


TODO:
- script para popular la db
  * Agregar Categoria
  * Agregar Grupo
  * Agregar Producto
- listar productos haciendo diferenciacion por categoria y/o tipo
- modelo de pedido
- vista para cargar 1 pedido
- vista de cocina
- modelo de mesa
- vista cliente carga pedido desde mesa
- cierre de mesa?
