# Generated by Django 3.1 on 2021-08-31 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='categorias.categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consigna', models.TextField(verbose_name='Texto de la pregunta')),
                ('max_puntaje', models.DecimalField(decimal_places=2, default=3, max_digits=6, verbose_name='Maximo Puntaje')),
                ('categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='la_categoria', to='categorias.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='PreguntaPartida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correcta', models.BooleanField(default=False, verbose_name='¿Es esta la respuesta correcta?')),
                ('partida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partida', to='preguntas.partida')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pregunta', to='preguntas.preguntas')),
            ],
        ),
        migrations.CreateModel(
            name='ElegirRespuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correcta', models.BooleanField(default=False, verbose_name='¿Es esta la respuesta correcta?')),
                ('texto', models.TextField(verbose_name='Texto de la respuesta')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas', to='preguntas.preguntas')),
            ],
        ),
    ]
