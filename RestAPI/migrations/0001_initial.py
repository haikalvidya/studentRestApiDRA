# Generated by Django 3.0.7 on 2021-09-10 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CRUDApi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('collage', models.CharField(max_length=70)),
                ('gender', models.BooleanField()),
            ],
        ),
    ]