# Generated by Django 4.0.6 on 2022-07-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('telefone', models.CharField(blank=True, max_length=11, null=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('senha', models.CharField(max_length=20)),
            ],
        ),
    ]
