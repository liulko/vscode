# Generated by Django 5.1.6 on 2025-02-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_calendarplan_subject_alter_calendarplan_class_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarplan',
            name='class_group',
            field=models.CharField(choices=[('5', '5-й клас'), ('7', '7-й клас'), ('8', '8-й клас'), ('9', '9-й клас')], max_length=50, verbose_name='Клас'),
        ),
        migrations.AlterField(
            model_name='calendarplan',
            name='subject',
            field=models.CharField(choices=[('Математика', 'Математика'), ('Алгебра', 'Алгебра'), ('Геометрія', 'Геометрія')], max_length=50, verbose_name='Предмет'),
        ),
    ]
