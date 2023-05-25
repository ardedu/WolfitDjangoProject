# Generated by Django 4.2 on 2023-05-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('description', models.CharField(max_length=250, verbose_name='Description')),
                ('full_text', models.TextField(verbose_name='Le contenu')),
                ('date', models.DateField(verbose_name='Date de publication')),
            ],
        ),
    ]
