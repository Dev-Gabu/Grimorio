# Generated by Django 5.0.6 on 2024-06-12 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sistema', models.SmallIntegerField(choices=[(1, 'Dungeons and Dragons'), (2, 'Tormenta'), (3, 'Ordem Paranormal'), (4, 'WilderFeast'), (5, 'Pokemon Tabletop Adventures')])),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fichas/fotos')),
            ],
        ),
    ]
