# Generated by Django 2.2 on 2020-01-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parlour', '0012_auto_20200125_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinment',
            name='Remark',
            field=models.IntegerField(blank=True, choices=[('1', 'Accepted'), ('0', 'Rejected')]),
        ),
    ]
