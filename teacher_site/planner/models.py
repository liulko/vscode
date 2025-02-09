from django.db import models

class CalendarPlan(models.Model):
    CLASS_CHOICES = [
        ('5', '5-й клас'),
        ('7', '7-й клас'),
        ('8', '8-й клас'),
        ('9', '9-й клас'),
    ]

    SUBJECT_CHOICES = [
        ('Математика', 'Математика'),
        ('Алгебра', 'Алгебра'),
        ('Геометрія', 'Геометрія'),
    ]

    date = models.DateField("Дата уроку")
    class_group = models.CharField("Клас", max_length=50, choices=CLASS_CHOICES)
    subject = models.CharField("Предмет", max_length=50, choices=SUBJECT_CHOICES)
    topic = models.CharField("Тема уроку", max_length=200)
    goal = models.TextField("Мета уроку")
    lesson_type = models.CharField("Тип уроку", max_length=50)
    materials = models.TextField("Матеріали", blank=True)
    homework = models.TextField("Домашнє завдання", blank=True)
    notes = models.TextField("Примітки", blank=True)

    def __str__(self):
        return f"{self.date} - {self.class_group} ({self.subject}): {self.topic}"