from django.test import TestCase


class EmptyDatabasePageTests(TestCase):
    def test_homepage_renders_without_database_records(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['skills_list'], [])
        self.assertIsNone(response.context['portfolio'])
        self.assertIsNone(response.context['social'])

    def test_projects_page_renders_without_database_records(self):
        response = self.client.get('/all-projects/')

        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context['portfolio'])
        self.assertIsNone(response.context['social'])
