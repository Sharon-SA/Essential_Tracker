from django.db import models
from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth.models import User

month_choice = [(
    'Jan', 'January'), ('Feb', 'February'), ('Mar', 'March'), ('Apr', 'April'), ('May', 'May'), ('Jun', 'June'),
    ('Jul', 'July'), ('Aug', 'August'), ('Sep', 'September'), ('Oct', 'October'), ('Nov', 'November'),
    ('Dec', 'December')]


class Expense(models.Model):
    payment_type = [('CH', 'Cash'), ('CR', 'Credit'), ('DB', 'Debit')]
    month = models.CharField(max_length=10, choices=month_choice)
    store = models.CharField(max_length=50)
    classification = models.CharField(max_length=50)
    items = models.TextField()
    method_of_payment = models.CharField(max_length=10, choices=payment_type)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount)


class Income(models.Model):
    month = models.CharField(max_length=10, choices=month_choice)
    # month = models.Field.unique_for_month
    salary = models.DecimalField(max_digits=100, decimal_places=2)
    investment = models.DecimalField(max_digits=100, decimal_places=2)
    credit_balance = models.DecimalField(max_digits=100, decimal_places=2)

    def total(self):
        return self.salary + self.investment + self.credit_balance

    def __str__(self):
        return str(self.total())


class Report(models.Model):
    month = models.CharField(max_length=10, choices=month_choice)
    total_income = models.IntegerField()
    total_expense = models.IntegerField()

    def net_income(self):
        return self.total_income - self.total_expense

    def __str__(self):
        return str(self.net_income())
