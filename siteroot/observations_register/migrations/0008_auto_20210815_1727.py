# Generated by Django 3.1.5 on 2021-08-15 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations_register', '0007_auto_20210815_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='eyes_col',
            field=models.CharField(choices=[('ГОЛУБОЙ', 'Голубой'), ('СЕРЫЙ', 'Серый'), ('ЗЕЛЕНЫЙ', 'Зеленый'), ('КАРИЙ', 'Карий')], max_length=7),
        ),
        migrations.AlterField(
            model_name='patient',
            name='hair_col',
            field=models.CharField(choices=[('БЛОНДИН', 'Блондин'), ('РЫЖИЙ', 'Рыжий'), ('ТЕМНЫЙ', 'Темный'), ('ЧЕРНЫЙ', 'Черный')], max_length=7),
        ),
    ]
