from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
    return render(request, 'register.html', {'form': form})

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
    return render(request, 'profile.html')

@login_required
def settings_view(request):
    return render(request, 'settings.html')

@login_required
def change_password_view(request):
    return render(request, 'change_password.html')

@login_required
def delete_account_view(request):
    return render(request, 'delete_account.html')

@login_required
def update_profile_view(request):
    return render(request, 'update_profile.html')

@login_required
def add_entry_view(request):
    return render(request, 'add_entry.html')

@login_required
def entry_edit_view(request, entry_id):
    return render(request, 'entry_edit.html', {'entry_id': entry_id})

@login_required
def entry_delete_view(request, entry_id):
    return render(request, 'entry_delete.html', {'entry_id': entry_id})

@login_required
def entry_detail_view(request, entry_id):
    return render(request, 'entry_detail.html', {'entry_id': entry_id})

@login_required
def transactions_view(request):
    return render(request, 'transactions.html')

@login_required
def add_transaction_view(request):
    return render(request, 'add_transaction.html')

@login_required
def edit_transaction_view(request, transaction_id):
    return render(request, 'edit_transaction.html', {'transaction_id': transaction_id})

@login_required
def delete_transaction_view(request, transaction_id):
    return render(request, 'delete_transaction.html', {'transaction_id': transaction_id})

@login_required
def transaction_detail_view(request, transaction_id):
    return render(request, 'transaction_detail.html', {'transaction_id': transaction_id})

@login_required
def budgets_view(request):
    return render(request, 'budgets.html')

@login_required
def add_budget_view(request):
    return render(request, 'add_budget.html')

@login_required
def edit_budget_view(request, budget_id):
    return render(request, 'edit_budget.html', {'budget_id': budget_id})

@login_required
def delete_budget_view(request, budget_id):
    return render(request, 'delete_budget.html', {'budget_id': budget_id})

@login_required
def budget_detail_view(request, budget_id):
    return render(request, 'budget_detail.html', {'budget_id': budget_id})

@login_required
def reports_view(request):
    return render(request, 'reports.html')

@login_required
def export_report_view(request):
    return render(request, 'export_report.html')

@login_required
def cards_view(request):
    return render(request, 'cards_accounts.html')

@login_required
def add_card_view(request):
    return render(request, 'add_card_account.html')

@login_required
def edit_card_view(request, card_account_id):
    return render(request, 'edit_card_account.html', {'card_account_id': card_account_id})

@login_required
def delete_card_view(request, card_account_id):
    return render(request, 'delete_card_account.html', {'card_account_id': card_account_id})

@login_required
def card_detail_view(request, card_account_id):
    return render(request, 'card_account_details.html', {'card_account_id': card_account_id})

@login_required
def income_view(request):
    return render(request, 'income.html')

@login_required
def add_income_view(request):
    return render(request, 'add_income.html')

@login_required
def edit_income_view(request, income_id):
    return render(request, 'edit_income.html', {'income_id': income_id})

@login_required
def delete_income_view(request, income_id):
    return render(request, 'delete_income.html', {'income_id': income_id})

@login_required
def income_detail_view(request, income_id):
    return render(request, 'income_details.html', {'income_id': income_id})

@login_required
def expenses_view(request):
    return render(request, 'expenses.html')

@login_required
def add_expense_view(request):
    return render(request, 'add_expense.html')

@login_required
def edit_expense_view(request, expense_id):
    return render(request, 'edit_expense.html', {'expense_id': expense_id})

@login_required
def delete_expense_view(request, expense_id):
    return render(request, 'delete_expense.html', {'expense_id': expense_id})

@login_required
def expense_detail_view(request, expense_id):
    return render(request, 'expense_details.html', {'expense_id': expense_id})

@login_required
def savings_view(request):
    return render(request, 'savings.html')

@login_required
def add_saving_view(request):
    return render(request, 'add_saving.html')

@login_required
def edit_saving_view(request, saving_id):
    return render(request, 'edit_saving.html', {'saving_id': saving_id})

@login_required
def delete_saving_view(request, saving_id):
    return render(request, 'delete_saving.html', {'saving_id': saving_id})

@login_required
def saving_detail_view(request, saving_id):
    return render(request, 'saving_details.html', {'saving_id': saving_id})





