# Generated by Django 3.2.9 on 2021-12-12 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pulse', '0002_alter_pulse_labeled'),
    ]

    operations = [
        migrations.AddField(
            model_name='pulse',
            name='Preprocessed',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
