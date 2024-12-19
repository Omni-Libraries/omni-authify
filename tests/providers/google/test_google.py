import unittest
from unittest.mock import patch
from omni_authify.providers.google import Google
from omni_authify import settings


class TestGoogle(unittest.TestCase):
    def setUp(self):
        self.client_id = settings.google_client_id
        self.client_secret = settings.google_client_secret
        self.redirect_uri = settings.google_redirect_uri
        self.scope = "openid%20email%20profile"
        self.provider = Google(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            scope=self.scope,
        )

    def test_initialization(self):
        self.assertEqual(self.provider.client_id, self.client_id)
        self.assertEqual(self.provider.client_secret, self.client_secret)
        self.assertEqual(self.provider.redirect_uri, self.redirect_uri)
        self.assertEqual(self.provider.scope, self.scope)

    @patch('requests.get')
    def test_get_access_token(self, mock_get):

        # Mock response
        mock_response = mock_get.return_value
        mock_response.raise_for_status = lambda: None
        mock_response.json.return_value = {"access_token": "test_access_token"}

        # Call the method
        access_token = self.provider.get_access_token()

        self.assertEqual(access_token, "test_access_token")

        mock_get.assert_called_with(self.provider.TOKEN_URL.format(client_id=self.client_id, redirect_uri=self.redirect_uri, scope=self.scope))

    @patch('requests.get')
    def test_get_user_profile(self, mock_get):
        access_token = "test_access_token"

        # Mock response
        mock_response = mock_get.return_value
        mock_response.raise_for_status = lambda: None
        mock_response.json.return_value = {
            "id": "1234567890",
            "name": "Test User",
            "email": "test@example.com",
            "picture": "https://example.com/picture.jpg",
        }

        # Call the method
        user_info = self.provider.get_user_profile(access_token)

        self.assertEqual(user_info["name"], "Test User")
        self.assertEqual(user_info["email"], "test@example.com")
        self.assertEqual(user_info["picture"], "https://example.com/picture.jpg")

        # Ensure the correct URL and params were used
        mock_get.assert_called_with(
            self.provider.PROFILE_URL.format(access_token=access_token))


if __name__ == "__main__":
    unittest.main()
