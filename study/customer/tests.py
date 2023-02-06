from authphone.models import AuthPhone
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Customer


class TestSignup(APITestCase):

    def setUp(self):
        self.signup_url = '/customer/signup/'
        self.auth_info_url = '/authphone/'
        self.email = 'test@naver.com'
        self.nickname = 'nicktest'
        self.password = 'testpassword!@#'
        self.name = 'testname'
        self.phone = '01012345678'
        self.empty_phone = '01098765432'

        self.correct_auth_info_params = {
            'phone': self.phone
        }

        self.correct_customer_params = {
            'email': self.email,
            'nickname': self.nickname,
            'password': self.password,
            'name': self.name,
            'phone': self.phone
        }

        self.incorrect_phone_customer_params = {
            'email': self.email,
            'nickname': self.nickname,
            'password': self.password,
            'name': self.name,
            'phone': self.empty_phone
        }

        self.empty_email_customer_params = {
            'nickname': self.nickname,
            'password': self.password,
            'name': self.name,
            'phone': self.phone
        }

        self.empty_nickname_customer_params = {
            'email': self.email,
            'password': self.password,
            'name': self.name,
            'phone': self.phone
        }

        self.empty_password_customer_params = {
            'email': self.email,
            'nickname': self.nickname,
            'name': self.name,
            'phone': self.phone
        }

        self.empty_name_customer_params = {
            'email': self.email,
            'nickname': self.nickname,
            'password': self.password,
            'phone': self.phone
        }

        self.empty_phone_customer_params = {
            'email': self.email,
            'nickname': self.nickname,
            'password': self.password,
            'name': self.name
        }

    def test_signup_empty_email_fail(self):
        response = self.client.post(self.signup_url, data=self.empty_email_customer_params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_empty_nickname_fail(self):
        response = self.client.post(self.signup_url, data=self.empty_nickname_customer_params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_empty_password_fail(self):
        response = self.client.post(self.signup_url, data=self.empty_password_customer_params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_empty_name_fail(self):
        response = self.client.post(self.signup_url, data=self.empty_name_customer_params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_empty_phone_fail(self):
        response = self.client.post(self.signup_url, data=self.empty_phone_customer_params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_check_auth_info_empty_fail(self):
        response = self.client.post(self.auth_info_url, data=self.correct_auth_info_params)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(self.signup_url, data=self.incorrect_phone_customer_params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_check_auth_info_by_is_success_fail(self):
        response = self.client.post(self.auth_info_url, data=self.correct_auth_info_params)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(self.signup_url, data=self.correct_customer_params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_success(self):
        # 전화번호 인증 요청
        response = self.client.post(self.auth_info_url, data=self.correct_auth_info_params)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # 전화번호 인증 전 성공여부 확인
        before_auth_info = AuthPhone.objects.get(phone=self.phone)
        self.assertEqual(before_auth_info.is_success, False)

        # 전화번호 인증 완료
        response = self.client.put(self.auth_info_url + str(before_auth_info.seq))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 전화번호 인증 후 성공여부 확인 및 인증 전 성공여부와 비교
        after_auth_info = AuthPhone.objects.get(seq=before_auth_info.seq)
        self.assertNotEqual(before_auth_info.is_success, after_auth_info.is_success)
        self.assertEqual(after_auth_info.is_success, True)

        # 회원 가입 요청
        response = self.client.post(self.signup_url, data=self.correct_customer_params)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # 회원 가입 시 작성된 데이터 비교
        customer = Customer.objects.get(email=self.email, nickname=self.nickname, password=self.password,
                                        name=self.name, phone=self.phone)
        self.assertEqual(customer.email, self.email)
        self.assertEqual(customer.nickname, self.nickname)
        self.assertEqual(customer.password, self.password)
        self.assertEqual(customer.name, self.name)
        self.assertEqual(customer.phone, self.phone)

    def tearDown(self):
        Customer.objects.all().delete()
        AuthPhone.objects.all().delete()


class TestSignin(APITestCase):
    def setUp(self):
        self.signup_url = '/customer/signup/'
        self.signin_url = '/customer/signin/'
        self.auth_info_url = '/authphone/'
        self.email = 'test@naver.com'
        self.nickname = 'nicktest'
        self.password = 'testpassword!@#'
        self.name = 'testname'
        self.phone = '01012345678'
        self.empty_phone = '01098765432'

        self.correct_auth_info_params = {
            'phone': self.phone
        }

        self.correct_customer_params = {
            'email': self.email,
            'nickname': self.nickname,
            'password': self.password,
            'name': self.name,
            'phone': self.phone
        }

        self.empty_password_customer_params = {
            'email': self.email,
            'nickname': self.nickname,
            'name': self.name,
            'phone': self.empty_phone
        }

        # 회원 가입 완료 상태
        self.client.post(self.auth_info_url, data=self.correct_auth_info_params)
        auth_info = AuthPhone.objects.get(phone=self.phone)
        self.client.put(self.auth_info_url + str(auth_info.seq))
        self.client.post(self.signup_url, data=self.correct_customer_params)

    def test_signin_empty_password(self):
        response = self.client.post(self.signin_url, data=self.empty_password_customer_params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signin_by_email_password(self):
        response = self.client.post(self.signin_url,
                                    data={'email': self.email, 'password': self.password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_signin_by_email_nickname_password(self):
        response = self.client.post(self.signin_url,
                                    data={'email': self.email, 'nickname': self.nickname, 'password': self.password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_signin_by_email_nickname_name_password(self):
        response = self.client.post(self.signin_url,
                                    data={'email': self.email, 'nickname': self.nickname, 'name': self.name,
                                          'password': self.password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_signin_by_email_nickname_name_phone_password(self):
        response = self.client.post(self.signin_url,
                                    data={'email': self.email, 'nickname': self.nickname, 'name': self.name,
                                          'phone': self.phone, 'password': self.password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_signin_by_nickname_password(self):
        response = self.client.post(self.signin_url,
                                    data={'nickname': self.nickname, 'password': self.password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_signin_by_nickname_name_password(self):
        response = self.client.post(self.signin_url,
                                    data={'nickname': self.nickname, 'name': self.name, 'password': self.password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_signin_by_nickname_name_phone_password(self):
        response = self.client.post(self.signin_url,
                                    data={'nickname': self.nickname, 'name': self.name,
                                          'phone': self.phone, 'password': self.password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_signin_by_name_password(self):
        response = self.client.post(self.signin_url,
                                    data={'name': self.name, 'password': self.password})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signin_by_name_phone_password(self):
        response = self.client.post(self.signin_url,
                                    data={'name': self.name, 'phone': self.phone, 'password': self.password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_signin_by_phone_password(self):
        response = self.client.post(self.signin_url,
                                    data={'phone': self.phone, 'password': self.password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self):
        Customer.objects.all().delete()
        AuthPhone.objects.all().delete()


class TestMypage(APITestCase):
    def setUp(self):
        self.signup_url = '/customer/signup/'
        self.mypage_url = '/customer/mypage/'
        self.auth_info_url = '/authphone/'
        self.email = 'test@naver.com'
        self.nickname = 'nicktest'
        self.password = 'testpassword!@#'
        self.name = 'testname'
        self.phone = '01012345678'
        self.empty_phone = '01098765432'

        self.correct_auth_info_params = {
            'phone': self.phone
        }

        self.correct_customer_params = {
            'email': self.email,
            'nickname': self.nickname,
            'password': self.password,
            'name': self.name,
            'phone': self.phone
        }

        # 회원 가입 완료 상태
        self.client.post(self.auth_info_url, data=self.correct_auth_info_params)
        auth_info = AuthPhone.objects.get(phone=self.phone)
        self.client.put(self.auth_info_url + str(auth_info.seq))
        self.client.post(self.signup_url, data=self.correct_customer_params)

    def test_mypage_empty_customer_fail(self):
        customer = Customer.objects.get(email=self.email, nickname=self.nickname, password=self.password,
                                        name=self.name, phone=self.phone)
        response = self.client.get(self.mypage_url + str(customer.seq + 1))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_mypage_success(self):
        customer = Customer.objects.get(email=self.email, nickname=self.nickname, password=self.password,
                                        name=self.name, phone=self.phone)
        response = self.client.get(self.mypage_url + str(customer.seq))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], customer.email)
        self.assertEqual(response.data['nickname'], customer.nickname)
        self.assertEqual(response.data['name'], customer.name)
        self.assertEqual(response.data['phone'], customer.phone)

    def tearDown(self):
        Customer.objects.all().delete()
        AuthPhone.objects.all().delete()


class TestChangePassword(APITestCase):
    def setUp(self):
        self.signup_url = '/customer/signup/'
        self.auth_info_url = '/authphone/'
        self.change_password_url = '/customer/password/'
        self.email = 'test@naver.com'
        self.nickname = 'nicktest'
        self.before_password = 'beforepassword!@#'
        self.after_password = 'afterpassword%^&'
        self.name = 'testname'
        self.phone = '01012345678'

        self.correct_auth_info_params = {
            'phone': self.phone
        }

        self.correct_customer_params = {
            'email': self.email,
            'nickname': self.nickname,
            'password': self.before_password,
            'name': self.name,
            'phone': self.phone
        }

        # 회원 가입 완료 상태
        self.client.post(self.auth_info_url, data=self.correct_auth_info_params)
        self.auth_info = AuthPhone.objects.get(phone=self.phone)
        self.client.put(self.auth_info_url + str(self.auth_info.seq))
        self.client.post(self.signup_url, data=self.correct_customer_params)

    def test_change_password_check_auth_info_is_success_fail(self):
        # 전화번호 재인증 시도
        response = self.client.put(self.auth_info_url + str(self.auth_info.seq))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        auth_info = AuthPhone.objects.get(phone=self.auth_info.phone)
        self.assertEqual(auth_info.is_success, False)

        # 비밀번호 변경
        response = self.client.put(self.change_password_url + str(self.auth_info.seq))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_change_password_success(self):
        # 전화번호 재인증 시도
        response = self.client.put(self.auth_info_url + str(self.auth_info.seq))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        auth_info = AuthPhone.objects.get(phone=self.auth_info.phone)
        self.assertEqual(auth_info.is_success, False)

        # 전화번호 재인증 완료
        response = self.client.put(self.auth_info_url + str(self.auth_info.seq))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        auth_info = AuthPhone.objects.get(phone=self.auth_info.phone)
        self.assertEqual(auth_info.is_success, True)

        # 비밀번호 변경
        response = self.client.put(self.change_password_url + str(self.auth_info.seq),
                                   data={'password': self.after_password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        customer = Customer.objects.get(email=self.email, nickname=self.nickname, password=self.after_password,
                                        name=self.name, phone=self.phone)
        self.assertEqual(customer.email, self.email)
        self.assertEqual(customer.nickname, self.nickname)
        self.assertEqual(customer.password, self.after_password)
        self.assertEqual(customer.name, self.name)
        self.assertEqual(customer.phone, self.phone)

    def tearDown(self):
        Customer.objects.all().delete()
        AuthPhone.objects.all().delete()
