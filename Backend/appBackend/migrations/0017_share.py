# Generated by Django 4.0.6 on 2023-01-16 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBackend', '0016_alter_group_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('share', models.IntegerField()),
            ],
        ),
    ]
