# Generated by Django 2.2 on 2020-09-15 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pkl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('nama', models.CharField(max_length=255)),
                ('alamat', models.CharField(max_length=255)),
                ('deskripsi', models.TextField(default='')),
                ('telp', models.CharField(max_length=255)),
            ],
        ),
    ]
