from django.contrib import admin
from .models import ExpenseCategory, DailyExpense

# Register your models here.
admin.site.register(ExpenseCategory)
admin.site.register(DailyExpense)
