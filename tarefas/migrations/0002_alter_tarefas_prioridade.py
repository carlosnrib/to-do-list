# Generated by Django 4.1.2 on 2022-10-24 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefas',
            name='prioridade',
            field=models.IntegerField(choices=[(0, 'NENHUMA'), (1, 'ALTA'), (2, 'MÉDIA'), (3, 'BAIXA')], default=0),
        ),
    ]