# Generated by Django 5.0.6 on 2024-05-13 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uav',
            old_name='weight',
            new_name='air_residence_time',
        ),
        migrations.AlterField(
            model_name='uav',
            name='brand',
            field=models.CharField(choices=[('Baykar', 'Baykar')], max_length=100),
        ),
    ]
