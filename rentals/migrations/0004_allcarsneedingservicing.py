# Generated by Django 4.1.7 on 2023-03-09 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0003_alter_car_last_serviced_millage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllCarsNeedingServicing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due', models.DateTimeField(auto_now_add=True)),
                ('note', models.CharField(blank=True, max_length=100)),
                ('serviced', models.BooleanField(default=False)),
                ('date_serviced', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.car')),
            ],
        ),
    ]
