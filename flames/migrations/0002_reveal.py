# Generated by Django 2.2.14 on 2022-06-29 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flames', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='reveal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('crush', models.CharField(max_length=50)),
            ],
        ),
    ]
