# Generated by Django 3.1.6 on 2021-02-03 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_card', '0003_auto_20210203_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='brand',
            field=models.CharField(blank=True, default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='cvv',
            field=models.IntegerField(blank=True),
        ),
    ]
