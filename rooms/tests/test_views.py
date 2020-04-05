import datetime

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse


from .. import views
from ..factories import AppointmentFactory, StaffMemberFactory, UserFactory


class LoginTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserFactory.create(username='user1')

    def test_user_can_login(self):
        response = self.client.login(username='user1', password='secret')
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)


class StaffIndexTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserFactory.create(username='user1')
        self.client.login(username='user1', password='secret')

    def test_view_status_code(self):
        response = self.client.get('/staff/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('rooms:staff-index'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('rooms:staff-index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/index.html')

    def test_view_contains_correct_html(self):
        response = self.client.get('/staff/')
        self.assertContains(
            response,
            '<h1 class="ui header">Liste der Mitarbeiter:innen</h1>')

    def test_view_contains_pagination(self):
        staff = StaffMemberFactory.create_batch(21)
        for m in staff:
            m.save()
        response = self.client.get('/staff/')
        self.assertContains(response, '<div class="ui pagination menu">')
        self.assertContains(response, 'class="item">2')


class AppointmentIndexTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserFactory.create(username='user1')
        self.client.login(username='user1', password='secret')

    def test_view_status_code(self):
        response = self.client.get('/appointments/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('rooms:appointment-index'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('rooms:appointment-index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointments/index.html')

    def test_view_contains_correct_html(self):
        response = self.client.get('/appointments/')
        self.assertContains(response, '<h1 class="ui header">Terminliste</h1>')

    def test_view_contains_pagination(self):
        appointments = AppointmentFactory.create_batch(21)
        for a in appointments:
            a.save()
        response = self.client.get('/appointments/')
        self.assertContains(response, '<div class="ui pagination menu">')
        self.assertContains(response, 'class="item">2')
