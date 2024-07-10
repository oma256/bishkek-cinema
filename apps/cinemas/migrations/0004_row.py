# Generated by Django 4.2.13 on 2024-07-10 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0003_hall'),
    ]

    operations = [
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Ряд')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hall', to='cinemas.hall', verbose_name='Зал')),
            ],
        ),
    ]
