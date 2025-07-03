from django.test import TestCase
from django.contrib.auth.models import User
from finance_tracker_app.models import Transaction, Category, Method, Profile, Budget

class CategoryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='catuser', password='testpass')

    def test_create_category(self):
        category = Category.objects.create(user=self.user, name='TestCategoryModel')
        self.assertEqual(category.name, 'TestCategoryModel')
        self.assertEqual(category.user, self.user)

class MethodModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='methoduser', password='testpass')

    def test_create_method(self):
        method = Method.objects.create(user=self.user, name='TestMethodModel')
        self.assertEqual(method.name, 'TestMethodModel')
        self.assertEqual(method.user, self.user)

class TransactionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='transuser', password='testpass')
        self.category = Category.objects.create(user=self.user, name='TestCategoryTransaction')
        self.method = Method.objects.create(user=self.user, name='TestMethodTransaction')

    def test_create_transaction(self):
        transaction = Transaction.objects.create(
            user=self.user,
            title='Cinema',
            amount=50,
            category=self.category,
            method=self.method,
            is_expense=True
        )
        self.assertEqual(transaction.title, 'Cinema')
        self.assertEqual(transaction.amount, 50)
        self.assertTrue(transaction.is_expense)
        self.assertEqual(transaction.category, self.category)
        self.assertEqual(transaction.method, self.method)

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='profileuser', password='testpass')

    def test_profile_created(self):
        self.assertTrue(hasattr(self.user, 'profile'))
        self.assertEqual(self.user.profile.currency, 'USD')

class BudgetModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='budgetuser', password='testpass')
        self.category = Category.objects.create(user=self.user, name='Groceries')

    def test_create_budget(self):
        budget = Budget.objects.create(user=self.user, name='Monthly Groceries', amount=300, category=self.category)
        self.assertEqual(budget.name, 'Monthly Groceries')
        self.assertEqual(budget.amount, 300)
        self.assertEqual(budget.category, self.category)
        self.assertEqual(budget.user, self.user)

