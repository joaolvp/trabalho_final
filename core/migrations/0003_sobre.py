# Generated by Django 4.0.5 on 2022-06-23 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_animal_options_alter_funcionario_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sobre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sobre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Sobre',
            },
        ),
    ]
