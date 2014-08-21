# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(unique=True, max_length=128)),
                ('descripcion', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(unique=True, max_length=128)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField(default=0)),
                ('categoria', models.ForeignKey(to='restoapp.Categoria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('estado', models.CharField(max_length=1, choices=[('P', 'PEDIDO'), ('C', 'COCINA'), ('M', 'MOSTRADOR'), ('D', 'DELIVERY'), ('E', 'ENTREGADO')])),
                ('fechahora', models.DateTimeField(auto_now_add=True)),
                ('menu', models.ManyToManyField(to='restoapp.Menu')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(unique=True, max_length=128)),
                ('descripcion', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='menu',
            name='presentacion',
            field=models.ForeignKey(to='restoapp.Presentacion'),
            preserve_default=True,
        ),
    ]
