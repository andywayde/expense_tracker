from django.db import models

import datetime


# Create your models here.
class Expense(models.Model):
    money_spent = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"On {self.date} we've spent {self.money_spent} GEL"

    class Meta:
        ordering = ["date"]
