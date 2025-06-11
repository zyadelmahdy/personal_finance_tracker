"""
URL configuration for finance_tracker_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from finance_tracker_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    #dashboard and user management
    path('', views.index_view, name='index'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('settings/', views.settings_view, name='settings'),
    path('settings/change_password/', views.change_password_view, name='change_password'),
    path('settings/delete_account/', views.delete_account_view, name='delete_account'),
    path('update_profile/', views.update_profile_view, name='update_profile'),
    
    
    #entry management
    path('add_entry/', views.add_entry_view, name='add_entry'),
    path('entry/<int:entry_id>/edit/', views.entry_edit_view, name='entry_edit'),
    path('entry/<int:entry_id>/delete/', views.entry_delete_view, name='entry_delete'),
    path('entry/<int:entry_id>/details/', views.entry_detail_view, name='entry_details'),
    
    
    #transaction management
    path('transactions/', views.transactions_view, name='transactions'),
    path('transactions/add/', views.add_transaction_view, name='add_transaction'),
    path('transactions/<int:transaction_id>/edit/', views.edit_transaction_view, name='edit_transaction'),
    path('transactions/<int:transaction_id>/delete/', views.delete_transaction_view, name='delete_transaction'),
    path('transactions/<int:transaction_id>/details/', views.transaction_detail_view, name='transaction_details'),
    
    
    #budget management
    path('budgets/', views.budgets_view, name='budgets'),
    path('budgets/add/', views.add_budget_view, name='add_budget'),
    path('budgets/<int:budget_id>/edit/', views.edit_budget_view, name='edit_budget'),
    path('budgets/<int:budget_id>/delete/', views.delete_budget_view, name='delete_budget'),
    path('budgets/<int:budget_id>/details/', views.budget_detail_view, name='budget_details'),
    
    
    #reporting management
    path('reports/', views.reports_view, name='reports'),
    path('export_report/', views.export_report_view, name='export_report'),
    
    
    #card and account management
    path('cards_accounts/', views.cards_view, name='cards_accounts'),
    path('cards_accounts/add/', views.add_card_view, name='add_card_account'),
    path('cards_accounts/<int:card_account_id>/edit/', views.edit_card_view, name='edit_card_account'),
    path('cards_accounts/<int:card_account_id>/delete/', views.delete_card_view, name='delete_card_account'),
    path('cards_accounts/<int:card_account_id>/details/', views.card_detail_view, name='card_account_details'),
    
    
    #income management
    path('income/', views.income_view, name='income'),
    path('income/add/', views.add_income_view, name='add_income'),
    path('income/<int:income_id>/edit/', views.edit_income_view, name='edit_income'),
    path('income/<int:income_id>/delete/', views.delete_income_view, name='delete_income'),
    path('income/<int:income_id>/details/', views.income_detail_view, name='income_details'),
    
    
    #expense management
    path('expenses/', views.expenses_view, name='expenses'),
    path('expenses/add/', views.add_expense_view, name='add_expense'),
    path('expenses/<int:expense_id>/edit/', views.edit_expense_view, name='edit_expense'),
    path('expenses/<int:expense_id>/delete/', views.delete_expense_view, name='delete_expense'),
    path('expenses/<int:expense_id>/details/', views.expense_detail_view, name='expense_details'),
    
    
    #savings management
    path('savings/', views.savings_view, name='savings'),
    path('savings/add/', views.add_saving_view, name='add_saving'),
    path('savings/<int:saving_id>/edit/', views.edit_saving_view, name='edit_saving'),
    path('savings/<int:saving_id>/delete/', views.delete_saving_view, name='delete_saving'),
    path('savings/<int:saving_id>/details/', views.saving_detail_view, name='saving_details'),
    
]
