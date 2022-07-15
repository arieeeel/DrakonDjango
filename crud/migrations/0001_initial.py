# Generated by Django 4.0.5 on 2022-06-29 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('idMarca', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
                ('precio', models.IntegerField(verbose_name='Precio Unitario')),
                ('stock', models.IntegerField(verbose_name='Stock')),
                ('imagen', models.ImageField(upload_to='', verbose_name='Imagen')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.marca')),
            ],
        ),
    ]
