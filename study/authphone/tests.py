from rest_framework import status
from rest_framework.test import APITestCase

from .models import AuthPhone


class TestSetAuthInfo(APITestCase):

    def setUp(self):
        self.base_url = '/authphone/'
        self.phone = '01012345678'
        self.empty_phone = '01098765432'

        self.correct_params = {
            'phone': self.phone
        }

    def test_set_auth_info_empty_phone_fail(self):
        response = self.client.post(self.base_url, data={})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_set_auth_info_already_saved_phone(self):
        response = self.client.post(self.base_url, data=self.correct_params)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(self.base_url, data=self.correct_params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_set_auth_info_success(self):
        response = self.client.post(self.base_url, data=self.correct_params)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        auth_info = AuthPhone.objects.get(phone=self.phone)
        self.assertEqual(auth_info.phone, self.phone)

    def tearDown(self):
        AuthPhone.objects.all().delete()


class TestUpdateAuthInfo(APITestCase):

    def setUp(self):
        self.base_url = '/authphone/'
        self.phone = '01012345678'
        self.empty_phone = '01098765432'

        self.correct_params = {
            'phone': self.phone
        }

    def test_set_auth_info_update_auth_info_fail(self):
        response = self.client.post(self.base_url, data=self.correct_params)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        before_auth_info = AuthPhone.objects.get(phone=self.phone)

        response = self.client.put(self.base_url + str(before_auth_info.seq + 1))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        after_auth_info = AuthPhone.objects.get(seq=before_auth_info.seq)
        self.assertEqual(before_auth_info.is_success, after_auth_info.is_success)
        self.assertEqual(after_auth_info.is_success, False)

    def test_set_auth_info_update_auth_info_success(self):
        response = self.client.post(self.base_url, data=self.correct_params)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        before_auth_info = AuthPhone.objects.get(phone=self.phone)
        self.assertEqual(before_auth_info.is_success, False)

        response = self.client.put(self.base_url + str(before_auth_info.seq))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        after_auth_info = AuthPhone.objects.get(seq=before_auth_info.seq)
        self.assertNotEqual(before_auth_info.is_success, after_auth_info.is_success)
        self.assertEqual(after_auth_info.is_success, True)

    def tearDown(self):
        AuthPhone.objects.all().delete()
