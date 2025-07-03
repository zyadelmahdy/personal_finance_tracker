from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Transaction, Category

class TransactionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(user=self.user, name='Food')

    def test_create_transaction(self):
        transaction = Transaction.objects.create(
            user=self.user,
            title='Groceries',
            amount=100,
            category=self.category,
            is_expense=True
        )
        self.assertEqual(transaction.title, 'Groceries')
        self.assertEqual(transaction.amount, 100)
        self.assertTrue(transaction.is_expense)
        self.assertEqual(transaction.category, self.category)
        self.assertEqual(transaction.user, self.user)
        self.assertIsNone(transaction.method)
        self.assertFalse(transaction.is_income)