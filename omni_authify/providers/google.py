from urllib.parse import urlencode

import requests

from .base import BaseOAuth2Provider


class Google(BaseOAuth2Provider):
    """
    Google OAuth2 provider.
    """
    TOKEN_URL: str = "https://accounts.google.com/o/oauth2/v2/auth?response_type=token&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}"
    PROFILE_URL: str = "https://www.googleapis.com/oauth2/v1/userinfo?access_token={access_token}"

    def __init__(self, client_id, client_secret, redirect_uri, scope):
        """
            Initialize the Google provider with client credentials.

            Args:
                client_id (str): The client ID provided by Google.
                client_secret (str): The client secret provided by Google.
                redirect_uri (str): The URI to redirect to after authentication.
        """
        super().__init__(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope, fields=["id"])
        
        
    def get_authorization_url(self, state=None, scope=None):
        return super().get_authorization_url(state, scope)


    def get_access_token(self) -> str:
        """
        Exchange the authorization code for an access token.

        Args:
            code (str): The authorization code received from the callback.

        Returns:
            str: The access token.
        """
        response = requests.get(self.TOKEN_URL.format(client_id=self.client_id, redirect_uri=self.redirect_uri, scope=self.scope))
        response.raise_for_status()
        return response.json().get("access_token")


    def get_user_profile(self, access_token: str) -> dict:
        """
        Fetch user profile information from Google.

        Args:
            access_token (str): The access token for the user.

        Returns:
            dict: The user profile data.
        """
        response = requests.get(self.PROFILE_URL.format(access_token=access_token))
        response.raise_for_status()
        return response.json()

