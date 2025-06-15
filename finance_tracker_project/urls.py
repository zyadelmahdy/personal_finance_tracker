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
from django.conf import settings
from django.conf.urls.static import static


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
    
    
    #payment method management
    path('methods/', views.method_view, name='methods'),
    path('add_method/', views.add_method_view, name='add_entry'),
    path('entry/<int:method_id>/edit/', views.edit_method_view, name='add_method'),
    path('entry/<int:method_id>/delete/', views.delete_method_view, name='delete_method'),
    path('entry/<int:method_id>/details/', views.method_details_view, name='method_details'),
    
    
    #transaction management
    path('transactions/', views.transactions_view, name='transactions'),
    path('transactions/add/', views.add_transaction_view, name='add_transaction'),
    path('transactions/<int:transaction_id>/edit/', views.edit_transaction_view, name='edit_transaction'),
    path('transactions/<int:transaction_id>/delete/', views.delete_transaction_view, name='delete_transaction'),
    path('transactions/<int:transaction_id>/details/', views.transaction_details_view, name='transaction_details'),
    path('add_category/', views.add_category_view, name='add_category'),
    path('categories/', views.categories_view, name='categories'),
    path('categories/<int:category_id>/edit/', views.edit_category_view, name='edit_category'),
    path('categories/<int:category_id>/delete/', views.delete_category_view, name='delete_category'),
    
    
    
    #budget management
    path('budgets/', views.budgets_view, name='budgets'),
    path('budgets/add/', views.add_budget_view, name='add_budget'),
    path('budgets/<int:budget_id>/edit/', views.edit_budget_view, name='edit_budget'),
    path('budgets/<int:budget_id>/delete/', views.delete_budget_view, name='delete_budget'),
    path('budgets/<int:budget_id>/details/', views.budget_details_view, name='budget_details'),
    
    
    #reporting management
    path('reports/', views.reports_view, name='reports'),
    path('export_report/', views.export_report_view, name='export_report'),
    
    
    #card and account management
    path('cards_accounts/', views.cards_accounts_view, name='cards_accounts'),
    path('cards_accounts/add/', views.add_card_account_view, name='add_card_account'),
    path('cards_accounts/<int:card_account_id>/edit/', views.edit_card_account_view, name='edit_card_account'),
    path('cards_accounts/<int:card_account_id>/delete/', views.delete_card_account_view, name='delete_card_account'),
    path('cards_accounts/<int:card_account_id>/details/', views.card_account_details_view, name='card_account_details'),
    
    
    #savings management
    path('savings/', views.savings_view, name='savings'),
    path('savings/add/', views.add_saving_view, name='add_saving'),
    path('savings/<int:saving_id>/edit/', views.edit_saving_view, name='edit_saving'),
    path('savings/<int:saving_id>/delete/', views.delete_saving_view, name='delete_saving'),
    path('savings/<int:saving_id>/details/', views.saving_detail_view, name='saving_details'),
    
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
