# Generated by Django 5.1.1 on 2024-09-26 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_joobmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joobmodel',
            name='ememployment_type',
            field=models.CharField(choices=[('full-time', 'FULL-TIME'), ('part-time', 'PART-TIME'), ('contract', 'Contract'), ('internship', 'Internship')], max_length=100, null=True),
        ),
    ]
