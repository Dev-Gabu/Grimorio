# Generated by Django 5.0.6 on 2024-06-24 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('rank', models.CharField(max_length=1)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='bestiario/fotos')),
                ('experiencia', models.SmallIntegerField(default=0)),
                ('doragos', models.SmallIntegerField(default=0)),
                ('elemento', models.SmallIntegerField(choices=[(1, 'Neutro'), (2, 'Piro'), (3, 'Aero'), (4, 'Geo'), (5, 'Hidro'), (6, 'Metalo'), (7, 'Electro'), (8, 'Fito'), (9, 'Crio'), (10, 'Umbra'), (11, 'Lumino'), (12, 'Cristalo'), (13, 'Vibro'), (14, 'Aether'), (15, 'Nether'), (16, 'Cosmo'), (17, 'Crono'), (18, 'Psycho')], default=0)),
            ],
        ),
    ]
