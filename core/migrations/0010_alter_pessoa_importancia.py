# Generated by Django 4.1.7 on 2023-04-11 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_pessoa_importancia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='importancia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.nivel'),
        ),
    ]