# Generated by Django 3.0.6 on 2020-05-26 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=17)),
                ('address', models.CharField(max_length=200)),
                ('projects', models.IntegerField()),
                ('images', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'Owner',
            },
        ),
    ]