# Generated by Django 3.2.6 on 2021-10-27 23:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('urlalias', '0002_urlalias_visitas'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestURLAlias',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('alias', models.TextField(unique=True)),
                ('fullurl', models.TextField()),
                ('visitas', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
