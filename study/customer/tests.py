from django.test import TestCase


class TestSignIn(TestCase):

    def setUp(self):
        self.email = 'test@naver.com'
        self.nick_name = 'nicktest'
        self.password = 'testpassword'
        self.name = 'test'
        self.phone = '01012345678'
