# Generated by Django 4.1.7 on 2023-04-07 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_pessoa_importancia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='importancia',
            field=models.CharField(db_column='importancia', max_length=2),
        ),
    ]
