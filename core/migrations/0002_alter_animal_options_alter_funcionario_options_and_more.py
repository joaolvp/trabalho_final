# Generated by Django 4.0.5 on 2022-06-22 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animal',
            options={'verbose_name': 'Animal', 'verbose_name_plural': 'Animais'},
        ),
        migrations.AlterModelOptions(
            name='funcionario',
            options={'verbose_name': 'Funcionário', 'verbose_name_plural': 'Funcionários'},
        ),
        migrations.AlterModelOptions(
            name='pet',
            options={'verbose_name': 'Pet', 'verbose_name_plural': 'Pets'},
        ),
    ]
