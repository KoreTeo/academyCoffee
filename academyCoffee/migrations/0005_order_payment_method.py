# Generated by Django 4.2.1 on 2023-06-18 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academyCoffee', '0004_remove_order_payment_method_user_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(default=1, max_length=20, verbose_name='Способ оплаты'),
            preserve_default=False,
        ),
    ]