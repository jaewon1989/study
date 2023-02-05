from rest_framework import status
from rest_framework.test import APITestCase

from .models import AuthPhone


class TestAuthPhone(APITestCase):

    def setUp(self):
        self.baseUrl = '/authphone/'
        self.phone = '01012345678'
        self.emptyPhone = '01098765432'
        self.auth_number = 7777

    def test_setAuthInfo_success(self):
        response = self.client.post(self.baseUrl, data={
            'phone': self.phone,
            'auth_number': self.auth_number
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        auth_phone_info = AuthPhone.objects.get(phone=self.phone, auth_number=self.auth_number)
        self.assertEqual(auth_phone_info.phone, self.phone)
        self.assertEqual(auth_phone_info.auth_number, self.auth_number)

    def test_setAuthInfo_already_saved_phone(self):
        response = self.client.post(self.baseUrl, data={
            'phone': self.phone,
            'auth_number': self.auth_number
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(self.baseUrl, data={
            'phone': self.phone,
            'auth_number': self.auth_number
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_setAuthInfo_empty_phone_fail(self):
        response = self.client.post(self.baseUrl, data={
            'auth_number': self.auth_number,
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_setAuthInfo_empty_auth_number_fail(self):
        response = self.client.post(self.baseUrl, data={
            'phone': self.phone
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_setAuthInfo_updateAuthInfoByPhone_success(self):
        self.client.post(self.baseUrl, data={
            'phone': self.phone,
            'auth_number': self.auth_number
        })

        before_auth_phone_info = AuthPhone.objects.get(phone=self.phone, auth_number=self.auth_number)
        self.assertEqual(before_auth_phone_info.is_success, False)

        response = self.client.put(self.baseUrl + str(before_auth_phone_info.seq))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        after_auth_phone_info = AuthPhone.objects.get(seq=before_auth_phone_info.seq)
        self.assertNotEqual(before_auth_phone_info.is_success, after_auth_phone_info.is_success)
        self.assertEqual(after_auth_phone_info.is_success, True)

    def test_setAuthInfo_updateAuthInfoByPhone_fail(self):
        self.client.post(self.baseUrl, data={
            'phone': self.phone,
            'auth_number': self.auth_number
        })

        before_auth_phone_info = AuthPhone.objects.get(phone=self.phone, auth_number=self.auth_number)

        response = self.client.put(self.baseUrl + str(before_auth_phone_info.seq + 1))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        after_auth_phone_info = AuthPhone.objects.get(seq=before_auth_phone_info.seq)
        self.assertEqual(before_auth_phone_info.is_success, after_auth_phone_info.is_success)
        self.assertEqual(after_auth_phone_info.is_success, False)

    def tearDown(self):
        AuthPhone.objects.all().delete()
