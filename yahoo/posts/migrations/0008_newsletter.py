# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-28 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_candle'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Qual o seu e-mail?', max_length=200)),
                ('Seu_nome', models.CharField(help_text='Qual o seu nome?', max_length=200)),
                ('itau', models.FileField(blank=True, help_text='Faça o upload do seu extrato', null=True, upload_to='documents/')),
                ('Setor', models.CharField(blank=True, choices=[('Serviço', 'Serviço'), ('Indústria', 'Indústria'), ('Agrobusiness', 'Agrobusiness'), ('Varejo', 'Varejo'), ('Financeiro', 'Financeiro'), ('Consultoria', 'Consultoria'), ('Tecnologia', 'Tecnologia')], help_text='Qual o seu segmento?', max_length=12, null=True)),
            ],
            managers=[
                ('pdobjects', django.db.models.manager.Manager()),
            ],
        ),
    ]
