# Generated by Django 5.0.3 on 2024-03-04 13:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Eintrag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=80, verbose_name='Eintrag')),
                ('done', models.BooleanField(default=False, verbose_name='Erledigt')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Erstellt')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name='Verändert')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Benutzer')),
            ],
            options={
                'verbose_name': 'Eintrag',
                'verbose_name_plural': 'Einträge',
            },
        ),
    ]
