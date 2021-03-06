# Generated by Django 3.1.3 on 2020-11-28 02:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Cashier', '0018_auto_20201116_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='is_theft',
        ),
        migrations.AddField(
            model_name='remainingcustomer',
            name='is_theft',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='/uploads/items/default.png', upload_to='uploads/items/5730f626-9f6d-4fc0-931f-dce57220f3f0/'),
        ),
        migrations.AlterField(
            model_name='remainingcustomer',
            name='enterTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 2, 4, 19, 620593, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='topuphistory',
            name='record',
            field=models.CharField(default='ECA9F233', max_length=8),
        ),
        migrations.AlterField(
            model_name='topuphistory',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 2, 4, 19, 620593, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 2, 4, 19, 620593, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.ImageField(default='/uploads/foto/default.png', upload_to='uploads/foto/8068b2fa-fef3-445a-bf62-ae8b825a3ba1/'),
        ),
    ]
