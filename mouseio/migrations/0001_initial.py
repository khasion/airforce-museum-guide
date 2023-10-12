# Generated by Django 4.2.1 on 2023-06-25 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('exhibit_ID', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('img', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LocationDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_trans', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=100000)),
                ('lang', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ExhibitDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100000)),
                ('lang', models.CharField(max_length=200)),
                ('exhibit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mouseio.exhibit')),
            ],
        ),
    ]
