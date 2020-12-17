# Generated by Django 3.1.3 on 2020-11-10 11:27

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Cashier', '0006_auto_20201110_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchant',
            name='barcode_enter',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='barcode_exit',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='barcode_payment',
        ),
        migrations.AlterField(
            model_name='enterhistory',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 10, 11, 20, 19, 547428, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='exithistory',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 10, 11, 20, 19, 547428, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='/uploads/items/default.png', upload_to='uploads/items/c0a31a6d-cdc0-49a8-aead-6810f6943f6f/'),
        ),
        migrations.AlterField(
            model_name='topuphistory',
            name='record',
            field=models.CharField(default='0FFD8C51', max_length=8),
        ),
        migrations.AlterField(
            model_name='topuphistory',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 10, 11, 20, 19, 547428, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 10, 11, 20, 19, 547428, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.ImageField(default='/uploads/foto/default.png', upload_to='uploads/foto/7a7649d5-3431-4723-8ad9-1710b40095b1/'),
        ),
        migrations.CreateModel(
            name='MerchantBarcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=500)),
                ('type', models.CharField(choices=[('ENTER', 'ENTER'), ('EXIT', 'EXIT'), ('PAY', 'PAY')], max_length=100)),
                ('merchants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cashier.merchant')),
            ],
        ),
        migrations.CreateModel(
            name='ItemBarcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=500)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cashier.item')),
            ],
        ),
    ]