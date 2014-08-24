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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=128, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=128, unique=True)),
                ('categoria', models.ForeignKey(to='restoapp.Categoria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=128, unique=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('descripcion', models.TextField(blank=True)),
                ('disponible', models.BooleanField(default=True)),
                ('grupo', models.ForeignKey(to='restoapp.Grupo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
