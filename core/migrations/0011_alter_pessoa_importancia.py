# Generated by Django 4.1.7 on 2023-04-11 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_pessoa_importancia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='importancia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.nivel'),
        ),
    ]