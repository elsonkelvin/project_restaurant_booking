from django.db import models
from django.contrib.auth.models import User

class Table(models.Model):
    table_number = models.IntegerField()
    seats = models.IntegerField()

    def __str__(self):
        return f"Table {self.table_number} ({self.seats} seats)"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    
    
    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"