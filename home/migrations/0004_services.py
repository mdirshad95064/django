# Generated by Django 4.0.6 on 2022-07-21 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=300)),
                ('descriptions', models.TextField()),
            ],
        ),
    ]