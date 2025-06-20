from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm, CategoryForm, MethodForm, ProfileForm, PreferencesForm, BudgetForm
from .models import Transaction, Profile, Budget
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum, Count
from datetime import datetime, timedelta
from django.utils import timezone
import csv

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
    context = {
        'form': form,
        'active_page': 'register',
    }
    return render(request, 'finance_tracker_app/register.html', context)

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
    context = {
        'form': form,
        'active_page': 'login',
    }
    return render(request, 'finance_tracker_app/login.html', context)

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('login')

# @login_required
# def profile_view(request):
#     return render(request, 'finance_tracker_app/profile.html')

@login_required
def settings_view(request):
    user = request.user
    profile = user.profile
    profile_form = ProfileForm(instance=profile, prefix='profile')
    preferences_form = PreferencesForm(instance=profile, prefix='preferences')
    password_form = PasswordChangeForm(user, prefix='password')

    if request.method == 'POST':
        if 'profile_submit' in request.POST:
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile, prefix='profile')
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, "Profile updated successfully.")
        elif 'preferences_submit' in request.POST:
            preferences_form = PreferencesForm(request.POST, instance=profile, prefix='preferences')
            if preferences_form.is_valid():
                preferences_form.save()
                messages.success(request, "Preferences updated successfully.")
        elif 'password_submit' in request.POST:
            password_form = PasswordChangeForm(user, request.POST, prefix='password')
            if password_form.is_valid():
                password_form.save()
                messages.success(request, "Password changed successfully.")

    context = {
        'profile_form': profile_form,
        'preferences_form': preferences_form,
        'password_form': password_form,
    }
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

    # Filter transactions by the current user
    if tab == 'income':
        transactions = Transaction.objects.filter(user=request.user, is_income=True).order_by(ordering)
    elif tab == 'expenses':
        transactions = Transaction.objects.filter(user=request.user, is_expense=True).order_by(ordering)
    else:
        transactions = Transaction.objects.filter(user=request.user).order_by(ordering)

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
            transaction.user = request.user  # Set the user
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
    transaction = get_object_or_404(Transaction, pk=transaction_id, user=request.user)
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
    transaction = get_object_or_404(Transaction, pk=transaction_id, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transactions')
    return render(request, 'finance_tracker_app/delete_transaction.html', {'transaction_id': transaction_id})

@login_required
def transaction_details_view(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id, user=request.user)  # Filter by user
    return render(request, 'finance_tracker_app/transaction_details.html', {'transaction_id': transaction_id})

@login_required
def budgets_view(request):
    budgets = Budget.objects.filter(user=request.user)
    context = {
        'active_page': 'budgets',
        'budgets': budgets,
    }
    return render(request, 'finance_tracker_app/budgets.html', context)

@login_required
def add_budget_view(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            messages.success(request, "Budget added successfully.")
            return redirect('budgets')
    else:
        form = BudgetForm()
    return render(request, 'finance_tracker_app/add_budget.html', {'form': form})

@login_required
def edit_budget_view(request, budget_id):
    budget = get_object_or_404(Budget, pk=budget_id, user=request.user)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            messages.success(request, "Budget updated successfully.")
            return redirect('budgets')
    else:
        form = BudgetForm(instance=budget)
    return render(request, 'finance_tracker_app/edit_budget.html', {'form': form, 'budget': budget})

@login_required
def delete_budget_view(request, budget_id):
    budget = get_object_or_404(Budget, pk=budget_id, user=request.user)
    if request.method == 'POST':
        budget.delete()
        messages.success(request, "Budget deleted successfully.")
        return redirect('budgets')
    return render(request, 'finance_tracker_app/delete_budget.html', {'budget': budget})

@login_required
def budget_details_view(request, budget_id):
    budget = get_object_or_404(Budget, pk=budget_id, user=request.user)
    return render(request, 'finance_tracker_app/budget_details.html', {'budget': budget})

@login_required
def reports_view(request):
    # Get date range (last 30 days by default)
    end_date = timezone.now()
    start_date = end_date - timedelta(days=30)
    
    # Get user's transactions
    user_transactions = Transaction.objects.filter(user=request.user, date__range=[start_date, end_date])
    
    # Income vs Expenses
    total_income = user_transactions.filter(is_income=True).aggregate(Sum('amount'))['amount__sum'] or 0
    total_expenses = user_transactions.filter(is_expense=True).aggregate(Sum('amount'))['amount__sum'] or 0
    net_income = total_income - total_expenses
    
    # Category breakdown for expenses
    expense_by_category = user_transactions.filter(is_expense=True).values('category__name').annotate(
        total=Sum('amount'),
        count=Count('id')
    ).order_by('-total')
    
    # Income by category
    income_by_category = user_transactions.filter(is_income=True).values('category__name').annotate(
        total=Sum('amount'),
        count=Count('id')
    ).order_by('-total')
    
    # Monthly trend (last 6 months)
    monthly_data = []
    for i in range(6):
        month_start = end_date.replace(day=1) - timedelta(days=30*i)
        month_end = month_start.replace(day=28) + timedelta(days=4)
        month_end = month_end.replace(day=1) - timedelta(days=1)
        
        month_income = user_transactions.filter(
            is_income=True, 
            date__year=month_start.year, 
            date__month=month_start.month
        ).aggregate(Sum('amount'))['amount__sum'] or 0
        
        month_expenses = user_transactions.filter(
            is_expense=True, 
            date__year=month_start.year, 
            date__month=month_start.month
        ).aggregate(Sum('amount'))['amount__sum'] or 0
        
        monthly_data.append({
            'month': month_start.strftime('%B %Y'),
            'income': month_income,
            'expenses': month_expenses,
            'net': month_income - month_expenses
        })
    
    # Budget analysis
    user_budgets = Budget.objects.filter(user=request.user)
    budget_analysis = []
    
    for budget in user_budgets:
        budget_spent = user_transactions.filter(
            is_expense=True,
            category=budget.category,
            date__range=[start_date, end_date]
        ).aggregate(Sum('amount'))['amount__sum'] or 0
        
        budget_remaining = budget.amount - budget_spent
        budget_percentage = (budget_spent / budget.amount * 100) if budget.amount > 0 else 0
        
        budget_analysis.append({
            'budget': budget,
            'spent': budget_spent,
            'remaining': budget_remaining,
            'percentage': budget_percentage,
            'status': 'over' if budget_spent > budget.amount else 'under' if budget_percentage < 80 else 'on_track'
        })
    
    # Top spending categories
    top_spending = expense_by_category[:5]
    
    # Recent transactions
    recent_transactions = user_transactions.order_by('-date')[:10]
    
    context = {
        'active_page': 'reports',
        'total_income': total_income,
        'total_expenses': total_expenses,
        'net_income': net_income,
        'expense_by_category': expense_by_category,
        'income_by_category': income_by_category,
        'monthly_data': monthly_data,
        'budget_analysis': budget_analysis,
        'top_spending': top_spending,
        'recent_transactions': recent_transactions,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'finance_tracker_app/reports.html', context)

@login_required
def export_report_view(request):
    # Get date range (last 30 days by default)
    end_date = timezone.now()
    start_date = end_date - timedelta(days=30)
    
    # Get user's transactions
    user_transactions = Transaction.objects.filter(user=request.user, date__range=[start_date, end_date])
    
    # Calculate summary data
    total_income = user_transactions.filter(is_income=True).aggregate(Sum('amount'))['amount__sum'] or 0
    total_expenses = user_transactions.filter(is_expense=True).aggregate(Sum('amount'))['amount__sum'] or 0
    net_income = total_income - total_expenses
    
    # Get budget analysis
    user_budgets = Budget.objects.filter(user=request.user)
    budget_analysis = []
    
    for budget in user_budgets:
        budget_spent = user_transactions.filter(
            is_expense=True,
            category=budget.category,
            date__range=[start_date, end_date]
        ).aggregate(Sum('amount'))['amount__sum'] or 0
        
        budget_remaining = budget.amount - budget_spent
        budget_percentage = (budget_spent / budget.amount * 100) if budget.amount > 0 else 0
        
        budget_analysis.append({
            'budget_name': budget.name,
            'category': budget.category.name,
            'budgeted': budget.amount,
            'spent': budget_spent,
            'remaining': budget_remaining,
            'percentage': budget_percentage,
        })
    
    # Get expense by category
    expense_by_category = user_transactions.filter(is_expense=True).values('category__name').annotate(
        total=Sum('amount'),
        count=Count('id')
    ).order_by('-total')
    
    # Get income by category
    income_by_category = user_transactions.filter(is_income=True).values('category__name').annotate(
        total=Sum('amount'),
        count=Count('id')
    ).order_by('-total')
    
    # Get monthly trend data
    monthly_data = []
    for i in range(6):
        month_start = end_date.replace(day=1) - timedelta(days=30*i)
        
        month_income = user_transactions.filter(
            is_income=True, 
            date__year=month_start.year, 
            date__month=month_start.month
        ).aggregate(Sum('amount'))['amount__sum'] or 0
        
        month_expenses = user_transactions.filter(
            is_expense=True, 
            date__year=month_start.year, 
            date__month=month_start.month
        ).aggregate(Sum('amount'))['amount__sum'] or 0
        
        monthly_data.append({
            'month': month_start.strftime('%B %Y'),
            'income': month_income,
            'expenses': month_expenses,
            'net': month_income - month_expenses
        })
    
    # Get recent transactions
    recent_transactions = user_transactions.order_by('-date')[:50]  # Export more transactions for CSV
    
    # Create CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="financial_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv"'
    
    writer = csv.writer(response)
    
    # Write summary section
    writer.writerow(['FINANCIAL SUMMARY'])
    writer.writerow(['Period', f'{start_date.strftime("%Y-%m-%d")} to {end_date.strftime("%Y-%m-%d")}'])
    writer.writerow(['Total Income', f'${total_income:.2f}'])
    writer.writerow(['Total Expenses', f'${total_expenses:.2f}'])
    writer.writerow(['Net Income', f'${net_income:.2f}'])
    writer.writerow([])
    
    # Write budget analysis
    if budget_analysis:
        writer.writerow(['BUDGET ANALYSIS'])
        writer.writerow(['Budget Name', 'Category', 'Budgeted Amount', 'Spent Amount', 'Remaining', 'Percentage Used'])
        for analysis in budget_analysis:
            writer.writerow([
                analysis['budget_name'],
                analysis['category'],
                f"${analysis['budgeted']:.2f}",
                f"${analysis['spent']:.2f}",
                f"${analysis['remaining']:.2f}",
                f"{analysis['percentage']:.1f}%"
            ])
        writer.writerow([])
    
    # Write expense by category
    if expense_by_category:
        writer.writerow(['EXPENSE BY CATEGORY'])
        writer.writerow(['Category', 'Total Amount', 'Transaction Count'])
        for category in expense_by_category:
            writer.writerow([
                category['category__name'] or 'Uncategorized',
                f"${category['total']:.2f}",
                category['count']
            ])
        writer.writerow([])
    
    # Write income by category
    if income_by_category:
        writer.writerow(['INCOME BY CATEGORY'])
        writer.writerow(['Category', 'Total Amount', 'Transaction Count'])
        for category in income_by_category:
            writer.writerow([
                category['category__name'] or 'Uncategorized',
                f"${category['total']:.2f}",
                category['count']
            ])
        writer.writerow([])
    
    # Write monthly trend
    if monthly_data:
        writer.writerow(['MONTHLY TREND (Last 6 Months)'])
        writer.writerow(['Month', 'Income', 'Expenses', 'Net'])
        for month in monthly_data:
            writer.writerow([
                month['month'],
                f"${month['income']:.2f}",
                f"${month['expenses']:.2f}",
                f"${month['net']:.2f}"
            ])
        writer.writerow([])
    
    # Write recent transactions
    if recent_transactions:
        writer.writerow(['RECENT TRANSACTIONS'])
        writer.writerow(['Title', 'Amount', 'Category', 'Type', 'Date', 'Description'])
        for transaction in recent_transactions:
            writer.writerow([
                transaction.title,
                f"${transaction.amount:.2f}",
                transaction.category.name if transaction.category else 'Uncategorized',
                'Income' if transaction.is_income else 'Expense' if transaction.is_expense else 'Unknown',
                transaction.date.strftime('%Y-%m-%d'),
                transaction.description
            ])
    
    return response

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
    referer_url = request.META.get('HTTP_REFERER', reverse('transactions'))
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            if 'from_modal' in request.POST:
                 return JsonResponse({'success': True, 'category_id': form.instance.id, 'category_name': form.instance.name})
            messages.success(request, 'Category added successfully!')
            return redirect(referer_url)
    else:
        form = CategoryForm()
    return render(request, 'finance_tracker_app/add_category.html', {
        'form': form,
        'referer_url': referer_url
    })

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