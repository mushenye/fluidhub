# Generated by Django 4.2.2 on 2023-07-28 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='passcode',
            field=models.CharField(default='169098AF3C08', max_length=12),
        ),
    ]