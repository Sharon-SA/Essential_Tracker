from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                          'registration/registration_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'registration/signup.html',
                  {'user_form': user_form})


@login_required
def dashboard(request):
    return render(request,
                  'essential/dashboard.html',
                  {'section': 'dashboard'})


@login_required
def expense_list(request):
    expenses = Expense.objects.filter(updated__lte=timezone.now())
    return render(request,
                  'essential/expense_list.html',
                  {'expenses': expenses})


@login_required
def expense_edit(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        # update
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.updated_date = timezone.now()
            expense.save()
            expense = Expense.objects.filter(updated__lte=timezone.now())
            return render(request, 'essential/expense_list.html',
                          {'expenses': expense})
    else:
        # edit
        form = ExpenseForm(instance=expense)
    return render(request, 'essential/expense_edit.html', {'form': form})


@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    expense.delete()
    return redirect('essential:expense_list')


@login_required
def expense_new(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.updated = timezone.now()
            expense.save()
            expenses = Expense.objects.filter(updated__lte=timezone.now())
            return render(request, 'essential/expense_list.html',
                          {'expenses': expenses})
    else:
        form = ExpenseForm()
        # print("Else")
    return render(request, 'essential/expense_new.html', {'form': form})


@login_required
def income_list(request):
    incomes = Income.objects.all
    return render(request,
                  'essential/income_list.html',
                  {'incomes': incomes})


@login_required
def income_edit(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == "POST":
        # update
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            income = form.save(commit=False)
            income.updated_date = timezone.now()
            income.save()
            income = Income.objects.all
            return render(request, 'essential/income_list.html',
                          {'incomes': income})
    else:
        # edit
        form = IncomeForm(instance=income)
    return render(request, 'essential/income_edit.html', {'form': form})


@login_required
def income_delete(request, pk):
    income = get_object_or_404(Income, pk=pk)
    income.delete()
    return redirect('essential:income_list')


@login_required
def income_new(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.created_date = timezone.now()
            income.save()
            incomes = Income.objects.all
            return render(request, 'essential/income_list.html',
                          {'incomes': incomes})
    else:
        form = IncomeForm()
        # print("Else")
    return render(request, 'essential/income_new.html', {'form': form})
