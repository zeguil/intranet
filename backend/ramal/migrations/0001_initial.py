# Generated by Django 4.0.3 on 2022-03-16 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('setor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ramal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsetor', models.CharField(max_length=60)),
                ('responsavel', models.CharField(max_length=120)),
                ('ramal', models.CharField(max_length=20)),
                ('state', models.IntegerField(default=0)),
                ('isBoss', models.BooleanField(default=False, null=True)),
                ('rank', models.IntegerField(null=True)),
                ('setor_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='setor.setor')),
            ],
        ),
    ]
