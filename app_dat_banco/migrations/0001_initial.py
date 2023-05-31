# Generated by Django 4.2.1 on 2023-05-31 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
                ('cpf', models.IntegerField(unique=True)),
                ('saldo', models.FloatField()),
            ],
        ),
    ]