# Generated by Django 2.2.3 on 2019-07-22 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('titulo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('autor', models.CharField(max_length=50)),
                ('bajada_titulo', models.CharField(max_length=50)),
                ('texto', models.TextField()),
                ('imagenes', models.ImageField(upload_to='static/noticias')),
                ('fechapublicacion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_comentario', models.TextField()),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Noticia')),
            ],
        ),
    ]