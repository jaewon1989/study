from rest_framework import status
from rest_framework.test import APITestCase

from .serializers import *


class TestAuthPhone(APITestCase):

    def setUp(self):
        self.phone = '01012345678'
        self.emptyPhone = '01098765432'
        self.auth_number = 7777
        self.baseUrl = '/authphone/'

    def test_setAuthInfo_success(self):
        response = self.client.post(self.baseUrl, data={
            'phone': self.phone,
            'auth_number': self.auth_number
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        authPhoneInfo = AuthPhone.objects.get(phone=self.phone)
        self.assertEqual(authPhoneInfo.phone, self.phone)
        self.assertEqual(authPhoneInfo.auth_number, self.auth_number)

    def test_setAuthInfo_empty_phone(self):
        response = self.client.post(self.baseUrl, data={
            'auth_number': self.auth_number,
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_setAuthInfo_empty_auth_number(self):
        response = self.client.post(self.baseUrl, data={
            'phone': self.phone
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_setAuthInfo_updateAuthInfoByPhone_success(self):
        self.client.post(self.baseUrl, data={
            'phone': self.phone,
            'auth_number': self.auth_number
        })

        beforeAuthPhoneInfo = AuthPhone.objects.get(phone=self.phone)
        self.assertEqual(beforeAuthPhoneInfo.is_success, False)

        response = self.client.put(self.baseUrl + self.phone)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        afterAuthPhoneInfo = AuthPhone.objects.get(phone=self.phone)
        self.assertNotEqual(beforeAuthPhoneInfo.is_success, afterAuthPhoneInfo.is_success)
        self.assertEqual(afterAuthPhoneInfo.is_success, True)

    def test_setAuthInfo_updateAuthInfoByPhone_fail(self):
        self.client.post(self.baseUrl, data={
            'phone': self.phone,
            'auth_number': self.auth_number
        })

        response = self.client.put(self.baseUrl + self.emptyPhone)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        authPhoneInfo = AuthPhone.objects.get(phone=self.phone)
        self.assertEqual(authPhoneInfo.is_success, False)

    def test_setAuthInfo_updateAuthInfoByPhone_getAuthInfoByPhone_success(self):
        self.client.post(self.baseUrl, data={
            'phone': self.phone,
            'auth_number': self.auth_number
        })

        self.client.put(self.baseUrl + self.phone)

        response = self.client.get(self.baseUrl + 'check/' + self.phone)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        authPhoneInfo = AuthPhone.objects.get(phone=self.phone)
        self.assertEqual(authPhoneInfo.is_success, True)

    def tearDown(self):
        AuthPhone.objects.all().delete()
