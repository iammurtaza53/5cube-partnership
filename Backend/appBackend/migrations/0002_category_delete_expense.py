# Generated by Django 4.0.6 on 2022-12-25 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBackend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(default='SOME STRING', max_length=100)),
                ('ctype', models.CharField(default='SOME STRING', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
    ]
