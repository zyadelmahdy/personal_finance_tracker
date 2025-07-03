from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Category, Method, Transaction, Budget

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='viewuser', password='testpass')
        self.category = Category.objects.create(user=self.user, name='TestCategoryView')
        self.method = Method.objects.create(user=self.user, name='TestMethodView')
        self.budget = Budget.objects.create(user=self.user, name='Test Budget', amount=100, category=self.category)
        self.transaction = Transaction.objects.create(user=self.user, title='Test', amount=10, category=self.category, method=self.method, is_expense=True)

    def test_login_required_views(self):
        protected_urls = [
            reverse('index'), reverse('settings'), reverse('budgets'), reverse('categories'), reverse('methods'),
            reverse('transactions'), reverse('add_transaction'), reverse('add_budget'), reverse('add_category'), reverse('add_method')
        ]
        for url in protected_urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_login_and_dashboard(self):
        login = self.client.login(username='viewuser', password='testpass')
        self.assertTrue(login)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dashboard')

    def test_add_transaction_view(self):
        self.client.login(username='viewuser', password='testpass')
        response = self.client.get(reverse('add_transaction'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add Transaction')

    def test_add_budget_view(self):
        self.client.login(username='viewuser', password='testpass')
        response = self.client.get(reverse('add_budget'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add Budget')

    def test_transactions_list(self):
        self.client.login(username='viewuser', password='testpass')
        response = self.client.get(reverse('transactions'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test')
