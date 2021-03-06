# Generated by Django 3.1.6 on 2021-06-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMList', '0003_auto_20210602_0906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='hvission',
            new_name='htcompany',
        ),
        migrations.AddField(
            model_name='branch',
            name='bemail',
            field=models.EmailField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='branch',
            name='bphone_number',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='company',
            name='hvision',
            field=models.TextField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='employee',
            name='gstatus',
            field=models.TextField(default=''),
        ),
    ]
