# Generated by Django 5.1.4 on 2025-01-14 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('discrption', models.TextField(max_length=200)),
            ],
        ),
    ]
