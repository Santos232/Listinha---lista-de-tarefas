# Generated by Django 4.1.7 on 2023-04-11 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_pessoa_importancia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='importancia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.nivel'),
        ),
    ]