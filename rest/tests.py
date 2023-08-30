from django.test import RequestFactory, TestCase
from django.urls import reverse
from rest.models import Kurulus
from rest.views import KurulusListView, KurulusViewSet, LoginView, RegisterView
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterViewTestCase(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()

    def test_register_user(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword",
            "password2": "testpassword"
        }
        request = self.factory.post('/register/', data, format='json')
        view = RegisterView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)


class LoginViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

    def test_login_user(self):
        data = {
            "username": "testuser",
            "password": "testpassword"
        }
        request = self.factory.post('/login/', data, format='json')
        view = LoginView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class KurulusViewSetTestCase(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.kurulus_data = {
            'name': 'Test Kurulus',
            'type': 'S',
            'country': 'TR',
            'date': '2023-08-30',
            'employees': 100
        }
        self.kurulus = Kurulus.objects.create(**self.kurulus_data)

    def test_kurulus_create(self):
        data = {
            'name': 'New Test Kurulus',
            'type': 'S',
            'country': 'IQ',
            'date': '2023-08-30',
            'employees': 150
        }
        request = self.factory.post('rest/kurulus/', data)
        view = KurulusViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Kurulus.objects.count(), 2)


class KurulusListViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.kurulus = Kurulus.objects.create(
            name='Test Kurulus',
            type='S',
            country='Test Country',
            date='2023-08-30',
            employees=100
        )

    def test_kurulus_list(self):
        request = self.factory.get('rest/kuruluslist/')
        view = KurulusListView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)