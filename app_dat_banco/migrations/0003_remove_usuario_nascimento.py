# Generated by Django 4.2.1 on 2023-05-31 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_dat_banco', '0002_usuario_delete_usuarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='nascimento',
        ),
    ]
