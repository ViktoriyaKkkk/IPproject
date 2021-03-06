# Generated by Django 3.2.5 on 2021-07-09 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210709_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=0)),
                ('passport', models.CharField(max_length=20, verbose_name='Паспорт')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('worker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='information', to='main.workers', verbose_name='Работник')),
            ],
            options={
                'verbose_name': 'Личная информация',
            },
        ),
    ]
