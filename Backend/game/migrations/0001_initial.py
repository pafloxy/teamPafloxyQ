# Generated by Django 4.1.1 on 2022-09-28 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GamePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n', models.PositiveIntegerField(blank=True, null=True)),
                ('bitstring', models.TextField(default='')),
            ],
        ),
    ]
