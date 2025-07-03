from django.test import TestCase
from django.contrib.auth.models import User
from finance_tracker_app.forms import TransactionForm, CategoryForm, MethodForm, BudgetForm
from finance_tracker_app.models import Category, Method

class TransactionFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='formuser', password='testpass')
        self.category = Category.objects.create(user=self.user, name='TestCategoryForm')
        self.method = Method.objects.create(user=self.user, name='TestMethodForm')

    def test_valid_transaction_form(self):
        form_data = {
            'title': 'Test',
            'amount': 10,
            'description': '',
            'category': self.category.id,
            'method': self.method.id
        }
        form = TransactionForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())

class CategoryFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='catformuser', password='testpass')

    def test_valid_category_form(self):
        form = CategoryForm(data={'name': 'UniqueTestCategoryForm'}, user=self.user)
        self.assertTrue(form.is_valid())

class MethodFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='methodformuser', password='testpass')

    def test_valid_method_form(self):
        form = MethodForm(data={'name': 'UniqueTestMethodForm'}, user=self.user)
        self.assertTrue(form.is_valid())

class BudgetFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='budgetformuser', password='testpass')
        self.category = Category.objects.create(user=self.user, name='Groceries')

    def test_valid_budget_form(self):
        form = BudgetForm(data={'name': 'Monthly', 'amount': 100, 'category': self.category.id}, user=self.user)
        self.assertTrue(form.is_valid())
