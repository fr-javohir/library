# Generated by Django 4.1.5 on 2023-01-09 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='qay_sana',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='record',
            name='talaba',
        ),
        migrations.AddField(
            model_name='record',
            name='talaba',
            field=models.ManyToManyField(to='asosiy.talaba'),
        ),
    ]
