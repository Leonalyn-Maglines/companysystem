# Generated by Django 3.1.6 on 2021-05-27 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LMList', '0003_auto_20210501_0724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kcontract_details', models.TextField(default='')),
                ('ktermination', models.TextField(default='')),
                ('kpromotions', models.TextField(default='')),
                ('position', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gwork_experience', models.TextField(default='')),
                ('gseminars_attended', models.TextField(default='')),
                ('gskills', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bcompany_branch', models.TextField(default='')),
                ('bcompany_address', models.TextField(default='')),
                ('bcontact_number', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hcompany_name', models.TextField(default='')),
                ('hdate_establish', models.TextField(default='')),
                ('hcompany_description', models.TextField(default='')),
                ('hmission', models.TextField(default='')),
                ('hvission', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qfull_name', models.TextField(default='')),
                ('qage', models.TextField(default='')),
                ('qaddress', models.TextField(default='')),
                ('gcollege', models.TextField(default='')),
                ('gsecondary_level', models.TextField(default='')),
                ('gprimary_level', models.TextField(default='')),
                ('qbranch', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='LMList.branch')),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='List',
        ),
        migrations.AddField(
            model_name='branch',
            name='bcompany',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='LMList.company'),
        ),
        migrations.AddField(
            model_name='background',
            name='gemployee',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='LMList.employee'),
        ),
        migrations.AddField(
            model_name='appointment_details',
            name='kemployee',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='LMList.employee'),
        ),
    ]
