# Generated by Django 3.0 on 2021-08-28 03:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('preguntas', '0011_partida_preguntapartida'),
    ]

    operations = [
        migrations.CreateModel(
            name='JuegosChacoUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje_total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Puntaje Total')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PreguntasRespondidas_preguntas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correcta', models.BooleanField(default=False, verbose_name='¿Es esta la respuesta correcta?')),
                ('puntaje_obtenido', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Puntaje Obtenido')),
                ('juegoschacoUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intentos', to='preguntas.JuegosChacoUsuario')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preguntas.Preguntas')),
                ('respuesta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='affectedDevice_repair', to='preguntas.ElegirRespuesta')),
            ],
        ),
    ]