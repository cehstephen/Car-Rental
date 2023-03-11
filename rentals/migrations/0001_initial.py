# Generated by Django 4.1.7 on 2023-03-07 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatteryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('due', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='EngineType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('service_criteria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='enginetype', to='rentals.servicecriteria')),
            ],
        ),
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('battery', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='battery', to='rentals.batterytype')),
                ('engine', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='engine', to='rentals.enginetype')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_service_date', models.DateField(auto_now=True)),
                ('current_millage', models.IntegerField(default=0, max_length=12)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('car_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rentals.cartype')),
            ],
        ),
        migrations.AddField(
            model_name='batterytype',
            name='service_criteria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='batterytype', to='rentals.servicecriteria'),
        ),
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='type', to='rentals.batterytype')),
            ],
        ),
    ]
