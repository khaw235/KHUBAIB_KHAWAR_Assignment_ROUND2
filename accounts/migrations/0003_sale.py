# Generated by Django 4.0.3 on 2022-04-06 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_detail_city_alter_detail_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(default='p', max_length=50)),
                ('revenue', models.CharField(default='p', max_length=50)),
                ('sales_number', models.IntegerField(default=0)),
            ],
        ),
    ]
