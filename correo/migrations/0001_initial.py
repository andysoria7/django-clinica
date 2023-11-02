# Generated by Django 4.2.6 on 2023-10-12 22:07

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroCorreoForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
                ('latitud', models.DecimalField(blank=True, decimal_places=15, max_digits=20, null=True)),
                ('longitud', models.DecimalField(blank=True, decimal_places=15, max_digits=20, null=True)),
                ('creado', models.DateTimeField(default=django.utils.timezone.now)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('usuarios', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
