# Generated by Django 3.0 on 2021-08-23 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('preguntas', '0002_auto_20210823_1533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preguntas',
            old_name='texto',
            new_name='consigna',
        ),
        migrations.AddField(
            model_name='preguntas',
            name='categorias',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='la_categoria', to='categorias.Categoria'),
            preserve_default=False,
        ),
    ]
