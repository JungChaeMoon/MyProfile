# Generated by Django 2.1.7 on 2019-06-15 21:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20190616_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 16, 6, 7, 55, 638232), verbose_name='date published'),
        ),
    ]
