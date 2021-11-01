from django.http import response
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import *

class RegistrationTestCase(APITestCase):
    data = {"username": "testcase", "email": "test@localhost.app",
                "password1": "strong_pass", "password2": "strong_pass"}

    def test_registration(self):
        response = self.client.post("/dj-rest-auth/registration/", self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        
        response = self.client.post("/dj-rest-auth/registration/", self.data)


        data = {
            "username": self.data["username"],
            "password": self.data["password1"]
        }
        response = self.client.post("/dj-rest-auth/login/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class AppTestCase(APITestCase):
    list_url = reverse("app-list")

    def setUp(self):
        self.post_data = {
            "name": "testCase",
            "description": "Descrition TestCase",
            "type": "Web",
            "framework": "Django",
            "domain_name": "test"
            }
        self.user = User.objects.create_user(username="johndoe",
                                             password="very-strong")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_app_create_authenticated(self):
        self.api_authentication()
        response = self.client.post("/api/v1/apps/", self.post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_app_create_un_authenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            "name": "testCase",
            "description": "Descrition TestCase",
            "type": "Web",
            "framework": "Django",
            "domain_name": "test"
            }

        response = self.client.post("/api/v1/apps/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_app_list_authenticated(self):
        self.api_authentication()
        response = self.client.post("/api/v1/apps/", self.post_data)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_app_detail_retrieve(self):
        self.api_authentication()
        response = self.client.post("/api/v1/apps/", self.post_data)
        appList = App.objects.all()
        response = self.client.get(reverse("app-detail", args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "testCase")


class PlanTestCase(APITestCase):
    list_url = reverse("plan-list")

    def setUp(self):
        self.user = User.objects.create_user(username="jeffdoe",
                                             password="very-strong")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_app_list_authenticated(self):
        Plan.objects.create(name='Free', description="dummy test")
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authenticated(self):
        Plan.objects.create(name='Free', description="dummy test")
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class SubscriptionTestCase(APITestCase):
    list_url = reverse("subscription-list")

    def setUp(self):
        self.user = User.objects.create_user(username="pauldoe",
                                             password="very-strong")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        App.objects.create(name="testCase2", description="Descrition TestCase", type="Web", framework="Django", domain_name="test", user=self.user)
        Plan.objects.create(name='Free', description="dummy test")

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_app_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_app_create_authenticated(self):
        self.api_authentication()
        data = {
            "plan": Plan.objects.get().id,
            "app": App.objects.get().id
            }

        response = self.client.post("/api/v1/subscriptions/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_app_create_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        data = {
            "plan": Plan.objects.get().id,
            "app": App.objects.get().id
            }

        response = self.client.post("/api/v1/subscriptions/", data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
