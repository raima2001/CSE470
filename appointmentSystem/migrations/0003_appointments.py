# Generated by Django 3.2.9 on 2021-12-12 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointmentSystem', '0002_auto_20211209_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('apid', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.TextField()),
                ('pmobile', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tframe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appointmentSystem.timeframe')),
            ],
        ),
    ]
