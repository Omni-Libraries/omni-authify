import unittest
from unittest.mock import patch
from urllib.parse import urlencode

from omni_authify import settings
from omni_authify.providers.facebook import Facebook


class TestFacebook(unittest.TestCase):
    def setUp(self):
        self.client_id = settings.client_id
        self.client_secret = settings.client_secret
        self.redirect_uri = settings.redirect_uri
        self.provider = Facebook(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            fields='id,name,email,picture',
            scope='your_strong_password'
        )

    def test_get_authorization_url(self):
        state = 'test_state'
        auth_url = self.provider.get_authorization_url(state=state)

        expected_params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "response_type": "code",
            "scope": "email,public_profile",
            "state": state,
        }

        expected_url = f"{self.provider.AUTHORIZE_URL}?{urlencode(expected_params)}"
        self.assertEqual(auth_url,expected_url)

    @patch('requests.get')
    def test_get_access_token(self, mock_get):
        code = "test_code"

        # ==== Mock response ====
        mock_response = mock_get.return_value
        mock_response.raise_for_status = lambda: None
        mock_response.json.return_value = {'access_token': 'test_access_token'}

        # ==== Call the method under the test ====
        access_token = self.provider.get_access_token(code=code)
        self.assertEqual(access_token, 'test_access_token')

        # ==== Ensure the correct URL and params were used ====
        mock_get.assert_called_with(
            self.provider.TOKEN_URL,
            params = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "redirect_uri": self.redirect_uri,
                "code": code,
            }
        )

    @patch('requests.get')
    def test_get_user_profile(self, mock_get):
        access_token = "test_access_token"

        # ==== Mock response ====
        mock_response = mock_get.return_value
        mock_response.raise_for_status = lambda: None
        mock_response.json.return_value = {
            'id': '1234567890',
            'name': 'Test User',
            'email': 'test@example.com',
            'picture': {'data': {'url': 'https://example.com/picture.jpg'}},
        }

        user_info = self.provider.get_user_profile(access_token=access_token)
        self.assertEqual(user_info['name'], 'Test User')
        self.assertEqual(user_info['email'], 'test@example.com')

        # ==== Ensure the correct URL and params were used ====
        mock_get.assert_called_with(
            self.provider.PROFILE_URL,
            params = {
                "access_token": access_token,
                "fields": "id,name,email,picture",
            }
        )

if __name__ == '__main__':
    unittest.main()











