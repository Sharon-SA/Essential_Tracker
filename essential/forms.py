from django import forms
from .models import Expense, Income, Report
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('month', 'store', 'classification', 'items', 'mop', 'amount')


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ('month', 'salary', 'investment', 'credit_balance')


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('month', 'total_income', 'total_expense')
