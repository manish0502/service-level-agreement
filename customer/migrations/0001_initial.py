# Generated by Django 2.2.7 on 2019-11-07 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SLA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_vendor', models.CharField(max_length=255)),
                ('sla_number', models.CharField(max_length=255)),
                ('sla_name', models.CharField(max_length=255)),
                ('sla', models.CharField(max_length=255)),
                ('kpi_threshold', models.IntegerField()),
            ],
        ),
    ]
