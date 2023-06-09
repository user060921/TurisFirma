# Generated by Django 4.2.1 on 2023-05-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turis_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutcarusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='des',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media')),
                ('percentage', models.FloatField(max_length=250)),
                ('country', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media')),
                ('country', models.CharField(max_length=250)),
                ('data', models.CharField(max_length=250)),
                ('people', models.CharField(max_length=250)),
                ('money', models.FloatField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media')),
                ('title', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='about',
            old_name='images',
            new_name='img',
        ),
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(),
        ),
    ]
