from urllib.parse import urlencode

import requests

from .base import BaseOAuth2Provider



class Google(BaseOAuth2Provider):
    """
    Google OAuth2 provider.
    """
    AUTHORIZE_URL: str = "https://accounts.google.com/o/oauth2/v2/auth"
    PROFILE_URL: str = "https://www.googleapis.com/oauth2/v1/userinfo"
    TOKEN_URL: str = "https://oauth2.googleapis.com/token"

    def __init__(self, client_id, client_secret, redirect_uri, scope):
        """
        Initialize the Google provider with client credentials.

        Args:
            client_id (str): The client ID provided by Google.
            client_secret (str): The client secret provided by Google (not used for service accounts).
            redirect_uri (str): The URI to redirect to after authentication.
            scope/fields (str): The comma-separated string of permissions requested.
        """
        super().__init__(
            client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, fields=['id'], scope=scope
            )

    def get_authorization_url(self, state=None, scope=None):
        """
        Generate the authorization URL to redirect the user for authentication.

        Returns:
            str: The authorization URL.
        """
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "response_type": "code",
            "scope": scope or self.scope
        }

        if state:
            params["state"] = state
        return f"{self.AUTHORIZE_URL}?{urlencode(params)}"

    def get_access_token(self, code):
        """
        Exchange the authorization code for an access token.

        Args:
            code (str): The authorization code received from the callback.

        Returns:
            str: The access token.
        """
        payload = {
            "grant_type": "authorization_code",
            "code": code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri,
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(self.TOKEN_URL, data=payload, headers=headers)
        response.raise_for_status()
        return  response.json().get("access_token")

    def get_user_profile(self, access_token, fields=None):
        """
        Fetch user profile information from Google.

        Args:
            access_token (str): The access token for the user.

        Returns:
            dict: The user profile data.
            :param access_token: from exchanging the code for an access token.
            :param fields: scope permissions for fetching user profile data.
        """
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(self.PROFILE_URL, headers=headers)
        response.raise_for_status()
        return response.json()


