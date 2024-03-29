# Generated by Django 3.2.4 on 2021-06-11 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CRM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(choices=[('binomio', 'Binomio'), ('bioingeniria', 'Bioingenieria'), ('centroQuirurgico', 'Centro Quirurgico'), ('ConsExternos-Imagenes-Hemodinamia', 'Cons Externos Imagenes-Hemodinamia')], default='bioingenieria', max_length=250)),
                ('requerimiento', models.CharField(choices=[('bioingenieria', 'Reparacion Bioingenieria'), ('edilicio', 'Reparacion Edilicio')], default='edilicio', max_length=250)),
                ('descripcion', models.TextField()),
                ('prioridad', models.CharField(choices=[('alta', 'Alta'), ('baja', 'Baja')], default='baja', max_length=100)),
            ],
        ),
    ]
