from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm, CategoryForm, MethodForm
from .models import Transaction

@login_required
def index_view(request):
    return render(request, 'finance_tracker_app/index.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('index')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, 'finance_tracker_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'finance_tracker_app/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('login')

@login_required
def profile_view(request):
    return render(request, 'finance_tracker_app/profile.html')

@login_required
def settings_view(request):
    context = {'active_page': 'settings'}
    return render(request, 'finance_tracker_app/settings.html', context)

@login_required
def change_password_view(request):
    return render(request, 'finance_tracker_app/change_password.html')

@login_required
def delete_account_view(request):
    return render(request, 'finance_tracker_app/delete_account.html')

@login_required
def update_profile_view(request):
    return render(request, 'finance_tracker_app/update_profile.html')

@login_required
def add_entry_view(request):
    return render(request, 'finance_tracker_app/add_entry.html')

@login_required
def entry_edit_view(request, entry_id):
    return render(request, 'finance_tracker_app/entry_edit.html', {'entry_id': entry_id})

@login_required
def entry_delete_view(request, entry_id):
    return render(request, 'finance_tracker_app/entry_delete.html', {'entry_id': entry_id})

@login_required
def entry_details_view(request, entry_id):
    return render(request, 'finance_tracker_app/entry_details.html', {'entry_id': entry_id})

@login_required
def transactions_view(request):
    tab = request.GET.get('tab', 'all')
    sort = request.GET.get('sort', 'date')
    order = request.GET.get('order', 'desc')

    if sort == 'category':
        ordering = 'category__name' if order == 'asc' else '-category__name'
    elif sort == 'method':
        ordering = 'method__name' if order == 'asc' else '-method__name'
    elif sort == 'type':
        # Sort by is_income first, then is_expense (so incomes come before expenses in asc)
        ordering = 'is_income' if order == 'asc' else '-is_income'
    else:
        ordering = sort if order == 'asc' else f'-{sort}'

    if tab == 'income':
        transactions = Transaction.objects.filter(is_income=True).order_by(ordering)
    elif tab == 'expenses':
        transactions = Transaction.objects.filter(is_expense=True).order_by(ordering)
    else:
        transactions = Transaction.objects.all().order_by(ordering)

    return render(request, 'finance_tracker_app/transactions.html', {
        'transactions': transactions,
        'tab': tab,
        'sort': sort,
        'order': order,
    })


@login_required
def add_transaction_view(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            t_type = request.POST.get('transaction_type')
            transaction.is_income = t_type == 'income'
            transaction.is_expense = t_type == 'expense'
            transaction.save()
            return redirect('transactions')
    else:
        form = TransactionForm()
    return render(request, 'finance_tracker_app/add_transaction.html', {'form': form})

@login_required
def edit_transaction_view(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            transaction = form.save(commit=False)
            t_type = request.POST.get('transaction_type')
            transaction.is_income = t_type == 'income'
            transaction.is_expense = t_type == 'expense'
            transaction.save()
            return redirect('transactions')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'finance_tracker_app/edit_transaction.html', {'form': form, 'transaction': transaction})

@login_required
def delete_transaction_view(request, transaction_id):
    return render(request, 'finance_tracker_app/delete_transaction.html', {'transaction_id': transaction_id})

@login_required
def transaction_details_view(request, transaction_id):
    return render(request, 'finance_tracker_app/transaction_details.html', {'transaction_id': transaction_id})

@login_required
def budgets_view(request):
    context = {
        'active_page': 'budgets',
    }
    return render(request, 'finance_tracker_app/budgets.html', context)

@login_required
def add_budget_view(request):
    return render(request, 'finance_tracker_app/add_budget.html')

@login_required
def edit_budget_view(request, budget_id):
    return render(request, 'finance_tracker_app/edit_budget.html', {'budget_id': budget_id})

@login_required
def delete_budget_view(request, budget_id):
    return render(request, 'finance_tracker_app/delete_budget.html', {'budget_id': budget_id})

@login_required
def budget_details_view(request, budget_id):
    return render(request, 'finance_tracker_app/budget_details.html', {'budget_id': budget_id})

@login_required
def reports_view(request):
    context = {
        'active_page': 'reports',
    }
    return render(request, 'finance_tracker_app/reports.html', context)

@login_required
def export_report_view(request):
    return render(request, 'finance_tracker_app/export_report.html')

@login_required
def cards_accounts_view(request):
    return render(request, 'finance_tracker_app/cards_accounts.html')

@login_required
def add_card_account_view(request):
    return render(request, 'finance_tracker_app/add_card_account.html')

@login_required
def edit_card_account_view(request, card_account_id):
    return render(request, 'finance_tracker_app/edit_card_account.html', {'card_account_id': card_account_id})

@login_required
def delete_card_account_view(request, card_account_id):
    return render(request, 'finance_tracker_app/delete_card_account.html', {'card_account_id': card_account_id})

@login_required
def card_account_details_view(request, card_account_id):
    return render(request, 'finance_tracker_app/card_account_details.html', {'card_account_id': card_account_id})

# @login_required
# def income_view(request):
#     transactions = Transaction.objects.filter(is_income=True)
#     return render(request, 'finance_tracker_app/income.html', {'transactions': transactions})

@login_required
def add_income_view(request):
    return render(request, 'finance_tracker_app/add_income.html')

@login_required
def edit_income_view(request, income_id):
    return render(request, 'finance_tracker_app/edit_income.html', {'income_id': income_id})

@login_required
def delete_income_view(request, income_id):
    return render(request, 'finance_tracker_app/delete_income.html', {'income_id': income_id})

@login_required
def income_details_view(request, income_id):
    return render(request, 'finance_tracker_app/income_details.html', {'income_id': income_id})



@login_required
def add_expense_view(request):
    return render(request, 'finance_tracker_app/add_expense.html')

@login_required
def edit_expense_view(request, expense_id):
    return render(request, 'finance_tracker_app/edit_expense.html', {'expense_id': expense_id})

@login_required
def delete_expense_view(request, expense_id):
    return render(request, 'finance_tracker_app/delete_expense.html', {'expense_id': expense_id})

@login_required
def expense_detail_view(request, expense_id):
    return render(request, 'finance_tracker_app/expense_details.html', {'expense_id': expense_id})

@login_required
def savings_view(request):
    return render(request, 'finance_tracker_app/savings.html')

@login_required
def add_saving_view(request):
    return render(request, 'finance_tracker_app/add_saving.html')

@login_required
def edit_saving_view(request, saving_id):
    return render(request, 'finance_tracker_app/edit_saving.html', {'saving_id': saving_id})

@login_required
def delete_saving_view(request, saving_id):
    return render(request, 'finance_tracker_app/delete_saving.html', {'saving_id': saving_id})

@login_required
def saving_detail_view(request, saving_id):
    return render(request, 'finance_tracker_app/saving_details.html', {'saving_id': saving_id})


@login_required
def categories_view(request):
    return render(request, 'finance_tracker_app/categories.html')

@login_required
def add_category_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_transaction')  # or wherever you want to go
    else:
        form = CategoryForm()
    return render(request, 'finance_tracker_app/add_category.html', {'form': form})

@login_required
def edit_category_view(request, category_id):
    return render(request, 'finance_tracker_app/edit_category.html', {'category_id': category_id})

@login_required
def delete_category_view(request, category_id):
    return render(request, 'finance_tracker_app/delete_category.html', {'category_id': category_id})



@login_required
def method_view(request):
    return render(request, 'finance_tracker_app/method.html')

@login_required
def add_method_view(request):
    if request.method == 'POST':
        form = MethodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_transaction')
    else:
        form = MethodForm()
    return render(request, 'finance_tracker_app/add_method.html', {'form': form})

@login_required
def edit_method_view(request, method_id):
    return render(request, 'finance_tracker_app/edit_method.html', {'method_id': method_id})

@login_required
def delete_method_view(request, method_id):
    return render(request, 'finance_tracker_app/delete_method.html', {'method_id': method_id})

@login_required
def method_details_view(request, method_id):
    return render(request, 'finance_tracker_app/method_details.html', {'method_id': method_id})