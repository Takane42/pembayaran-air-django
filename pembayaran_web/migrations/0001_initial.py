# Generated by Django 5.2.1 on 2025-05-09 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelanggan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_pelanggan', models.CharField(max_length=10)),
                ('nama', models.CharField(max_length=100)),
                ('alamat', models.TextField()),
                ('bulan', models.CharField(max_length=20)),
                ('meter_awal', models.IntegerField()),
                ('meter_akhir', models.IntegerField()),
            ],
        ),
    ]
