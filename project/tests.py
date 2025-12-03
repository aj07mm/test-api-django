"""Basic tests for the project."""
from django.test import TestCase
from django.urls import reverse


class BasicTestCase(TestCase):
    """Basic test cases to verify setup."""

    def test_admin_url_exists(self):
        """Test that the admin URL is accessible."""
        response = self.client.get(reverse('admin:index'))
        # Should redirect to login since we're not authenticated
        self.assertEqual(response.status_code, 302)

    def test_home_redirects(self):
        """Test that home redirects to admin."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin/', response.url)