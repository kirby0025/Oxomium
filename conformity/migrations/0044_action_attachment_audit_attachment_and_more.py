# Generated by Django 4.2.9 on 2024-10-12 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conformity', '0043_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='attachment',
            field=models.ManyToManyField(blank=True, related_name='actions', to='conformity.attachment'),
        ),
        migrations.AddField(
            model_name='audit',
            name='attachment',
            field=models.ManyToManyField(blank=True, related_name='audits', to='conformity.attachment'),
        ),
        migrations.AddField(
            model_name='controlpoint',
            name='attachment',
            field=models.ManyToManyField(blank=True, related_name='ControlPoint', to='conformity.attachment'),
        ),
        migrations.AddField(
            model_name='finding',
            name='attachment',
            field=models.ManyToManyField(blank=True, related_name='findings', to='conformity.attachment'),
        ),
        migrations.AddField(
            model_name='framework',
            name='attachment',
            field=models.ManyToManyField(blank=True, related_name='frameworks', to='conformity.attachment'),
        ),
        migrations.AddField(
            model_name='organization',
            name='attachment',
            field=models.ManyToManyField(blank=True, related_name='organizations', to='conformity.attachment'),
        ),
    ]
