# Generated by Django 5.0.1 on 2024-02-06 02:28

import AllUsers.models
import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0013_alter_group_id_alter_permission_id_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadPaymentModel',
            fields=[
                ('PaymentID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('PaymentImage', models.FileField(blank=True, null=True, upload_to='payment/Inovice/')),
                ('username', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Payment Upload',
                'verbose_name_plural': 'Payment Upload',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('role', models.CharField(blank=True, default='Resident', max_length=10, null=True)),
                ('HouseUnit', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('ParkingLot', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_groups', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_permissions', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'permissions': [('can_do_something', 'Can do something')],
                'default_related_name': 'custom_users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPaymentModel',
            fields=[
                ('InvoiceID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('PaymentAmount', models.CharField(default='0', max_length=20)),
                ('InvoiceDate', models.DateField(auto_now=True)),
                ('InvoiceTime', models.TimeField(auto_now=True)),
                ('InvoiceImage', models.ImageField(blank=True, null=True, upload_to='payment/')),
                ('paid', models.BooleanField(verbose_name='paid?')),
                ('InvoiceMonth', AllUsers.models.MonthField()),
                ('userID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payment',
            },
        ),
    ]
