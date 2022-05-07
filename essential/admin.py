from django.contrib import admin

from .models import Expense, Income, Report


@admin.register(Expense)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'month', 'store', 'classification', 'items', 'mop', 'amount')

@admin.register(Income)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'month', 'salary', 'investment', 'credit_balance', 'total')

@admin.register(Report)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'month', 'total_income', 'total_expense', 'net_income')
