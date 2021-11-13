# Generated by Django 3.2.9 on 2021-11-13 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('food', models.CharField(default='pizza', max_length=100)),
                ('calories', models.CharField(default='100', max_length=5)),
            ],
        ),
    ]
