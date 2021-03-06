# Generated by Django 3.1.2 on 2020-10-31 20:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('developer', models.TextField(max_length=200)),
                ('editor', models.TextField(max_length=200)),
                ('summary', models.TextField(help_text='Deja descripcion del Juego', max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='imgs/')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='book',
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='genre',
            name='summary',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ManyToManyField(to='catalogo.Genre'),
        ),
    ]
