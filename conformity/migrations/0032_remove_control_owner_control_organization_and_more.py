# Generated by Django 4.1.6 on 2023-02-25 20:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conformity', '0031_alter_control_frequency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='control',
            name='owner',
        ),
        migrations.AddField(
            model_name='control',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='conformity.organization'),
        ),
        migrations.AlterField(
            model_name='controlpoint',
            name='control_date',
            field=models.DateField(default=datetime.date(2023, 2, 25)),
        ),
    ]
