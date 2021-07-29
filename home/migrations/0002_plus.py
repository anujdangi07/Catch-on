# Generated by Django 3.2 on 2021-07-14 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plus',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=14)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=130)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]