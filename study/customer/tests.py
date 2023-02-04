from django.test import TestCase

from .models import Customer


class TestSignIn(TestCase):

    def setUp(self):
        self.email = 'test@naver.com'
        self.nick_name = 'nicktest'
        self.password = 'testpassword'
        self.name = 'test'
        self.phone = '01012345678'
        self.customer = Customer(
            email=self.email,
            nick_name=self.nick_name,
            password=self.password,
            name=self.name,
            phone=self.phone,
        )

    def test_model_can_create_a_bucketlist(self):
        old_count = Customer.objects.count()
        self.customer.save()
        new_count = Customer.objects.count()
        self.assertNotEqual(old_count, new_count)
