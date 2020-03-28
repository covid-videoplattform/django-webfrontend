import datetime

from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse

from .. import views


class StaffIndexTests(TestCase):

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


class AppointmentIndexTests(TestCase):

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
