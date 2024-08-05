from django.db import models

class Car(models.Model):
    
    # Ограничения для полей
    FUEL_CHOICES = [
        ('бензин', 'Бензин'),
        ('дизель', 'Дизель'),
        ('электричество', 'Электричество'),
        ('гибрид', 'Гибрид'),
    ]

    TRANSMISSION_CHOICES = [
        ('механическая', 'Механическая'),
        ('автоматическая', 'Автоматическая'),
        ('вариатор', 'Вариатор'),
        ('робот', 'Робот'),
    ]

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    mileage = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
