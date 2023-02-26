# Generated by Django 4.1.6 on 2023-02-25 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conformity', '0035_action_associated_controlpoints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlpoint',
            name='status',
            field=models.CharField(choices=[('SCHD', 'Scheduled'), ('TOBE', 'To evaluate'), ('OK', 'Compliant'), ('NOK', 'Non-Compliant'), ('MISS', 'Missed')], default='SCHD', max_length=4),
        ),
    ]
