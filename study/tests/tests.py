from django.apps import apps
from django.test import TestCase


# Create your tests here.
class TestSignIn(TestCase):
    def setUp(self):
        self.CustomerModel = apps.get_model('customer', 'Customer')
        self.email = 'test@naver.com'
        self.nick_name = 'nicktest'
        self.password = 'testpassword'
        self.name = 'test'
        self.phone = '01012345678'

        self.customer = self.CustomerModel(
            email=self.email,
            nick_name=self.nick_name,
            password=self.password,
            name=self.name,
            phone=self.phone,
        )

    def test_model_can_create_a_bucketlist(self):
        old_count = self.CustomerModel.objects.count()
        self.customer.save()
        new_count = self.CustomerModel.objects.count()
        self.assertNotEqual(old_count, new_count)
