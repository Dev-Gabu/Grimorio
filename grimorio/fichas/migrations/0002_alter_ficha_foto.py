# Generated by Django 5.0.6 on 2024-06-12 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='ficha/fotos'),
        ),
    ]
