# Generated by Django 4.2.1 on 2023-08-16 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mouseio', '0002_locationdescription_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationdescription',
            name='feat_img',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
