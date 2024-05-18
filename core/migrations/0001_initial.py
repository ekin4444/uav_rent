# Generated by Django 5.0.6 on 2024-05-13 13:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DateRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UAV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('Brand1', 'Brand 1'), ('Brand2', 'Brand 2'), ('Brand3', 'Brand 3')], max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.CharField(choices=[('Category1', 'Category 1'), ('Category2', 'Category 2'), ('Category3', 'Category 3')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RentalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Rented', 'Rented'), ('Returned', 'Returned'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('uav', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.uav')),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Rented', 'Rented'), ('Returned', 'Returned'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('uav', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.uav')),
            ],
        ),
        migrations.CreateModel(
            name='Lease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_range', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.daterange')),
                ('renter_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('uav', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.uav')),
            ],
        ),
    ]