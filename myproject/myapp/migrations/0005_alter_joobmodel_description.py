# Generated by Django 5.1.1 on 2024-09-26 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_joobmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joobmodel',
            name='description',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]
