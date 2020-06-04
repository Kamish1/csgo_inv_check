# Generated by Django 2.2 on 2020-06-01 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
                ('link_img', models.CharField(max_length=500, null=True)),
                ('link_inspect', models.CharField(max_length=500, null=True)),
                ('float', models.FloatField(null=True)),
                ('color', models.CharField(max_length=50, null=True)),
                ('trade_lock', models.CharField(max_length=100, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('class_item', models.CharField(max_length=50, null=True)),
                ('expiration_data', models.CharField(max_length=50, null=True)),
                ('price_av_week', models.IntegerField(null=True)),
                ('condition', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]