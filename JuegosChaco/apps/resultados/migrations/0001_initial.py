# Generated by Django 3.0 on 2021-08-25 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0002_puntajeusuario'),
        ('preguntas', '0009_auto_20210825_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreguntasRespondidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correcta', models.BooleanField(default=False, verbose_name='¿Es esta la respuesta correcta?')),
                ('puntaje_obtenido', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Puntaje Obtenido')),
                ('preguntas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preguntas.Preguntas')),
                ('respuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intentos', to='preguntas.ElegirRespuesta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.PuntajeUsuario')),
            ],
        ),
    ]