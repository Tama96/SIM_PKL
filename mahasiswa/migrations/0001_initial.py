# Generated by Django 3.1.1 on 2020-09-25 14:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mitra', '0002_auto_20200924_0259'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pkl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('dosen', models.CharField(default='', max_length=255)),
                ('tanggal_mulai', models.DateField(default=datetime.datetime.now)),
                ('tanggal_selesai', models.DateField()),
                ('approve', models.BooleanField(default=False)),
                ('nama_mitra', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mitra.mitra')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mahasiswa', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
