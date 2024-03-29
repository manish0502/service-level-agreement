# Generated by Django 2.2.7 on 2019-11-07 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20191107_0929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sla_number', models.CharField(max_length=255)),
                ('min', models.DecimalField(decimal_places=2, max_digits=3)),
                ('max', models.DecimalField(decimal_places=2, max_digits=3)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]
