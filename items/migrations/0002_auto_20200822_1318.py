# Generated by Django 3.0.8 on 2020-08-22 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('img', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.DeleteModel(
            name='cars',
        ),
    ]