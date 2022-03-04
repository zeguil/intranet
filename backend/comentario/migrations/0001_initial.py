# Generated by Django 4.0.3 on 2022-03-04 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_nome', models.CharField(max_length=60)),
                ('conteudo', models.TextField()),
                ('ano', models.DateField(default=2022)),
                ('data_env', models.DateField(auto_now_add=True)),
                ('state', models.IntegerField(default=0)),
                ('func_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionario.funcionario')),
            ],
        ),
    ]
