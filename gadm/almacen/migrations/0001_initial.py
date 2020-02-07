# Generated by Django 2.0.13 on 2020-02-01 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('costoVenta', models.DecimalField(decimal_places=4, max_digits=18)),
                ('impuestoVenta', models.DecimalField(decimal_places=4, max_digits=18)),
                ('alicuotaIva', models.DecimalField(decimal_places=2, max_digits=5)),
                ('margenVenta', models.DecimalField(decimal_places=4, max_digits=18)),
                ('precioVentaFinal', models.DecimalField(decimal_places=4, max_digits=18)),
            ],
        ),
        migrations.CreateModel(
            name='CondIvaOp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='condIva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.CondIvaOp'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='familia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.Familia'),
        ),
    ]
