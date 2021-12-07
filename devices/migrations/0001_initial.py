# Generated by Django 3.2.9 on 2021-12-06 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_of_device', models.CharField(max_length=100, unique=True)),
                ('Time_send', models.DateTimeField(auto_now=True)),
                ('labeled', models.CharField(max_length=100, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]