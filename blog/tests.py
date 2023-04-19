from django.test import TestCase, Client
from django.urls import reverse


class BlogViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse("index-page"))
        self.assertTemplateUsed(response, "blog/index.html")
        self.assertEqual(200, response.status_code)

    def test_about(self):
        response = self.client.get(reverse("about-view"))
        self.assertTemplateUsed(response, "blog/about.html")
        self.assertEqual(200, response.status_code)

    def test_contacts(self):
        response = self.client.get(reverse("contacts-view"))
        self.assertTemplateUsed(response, "blog/contacts.html")
        self.assertEqual(200, response.status_code)

    def test_post_update(self):
        response = self.client.get(reverse("post-update"))
        self.assertTemplateUsed("blog/post_update.html")
        self.assertEqual(200, response.status_code)

    def test_post_create(self):
        response = self.client.get(reverse("post-create"))
        self.assertTemplateUsed("blog/post_create.html")
        self.assertEqual(200, response.status_code)