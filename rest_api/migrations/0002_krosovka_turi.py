# Generated by Django 4.1.1 on 2022-10-07 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='krosovka',
            name='turi',
            field=models.CharField(choices=[('SPORT', 'Sport'), ('BAZM', 'Bazm')], default='SPORT', max_length=6),
        ),
    ]
