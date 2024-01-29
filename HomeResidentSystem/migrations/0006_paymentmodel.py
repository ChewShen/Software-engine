# Generated by Django 5.0 on 2024-01-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeResidentSystem', '0005_noticeboardmodel_noticeimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('PaymentID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('PaymentImage', models.FileField(blank=True, null=True, upload_to='payment/Inovice/')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payment',
            },
        ),
    ]
