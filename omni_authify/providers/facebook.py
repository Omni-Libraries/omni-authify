from urllib.parse import urlencode

import requests

from .base import BaseOAuth2Provider


class Facebook(BaseOAuth2Provider):
    """
    Facebook OAuth2 provider.
    """
    AUTHORIZE_URL: str = "https://www.facebook.com/v16.0/dialog/oauth"
    TOKEN_URL: str = "https://graph.facebook.com/v16.0/oauth/access_token"
    PROFILE_URL: str = "https://graph.facebook.com/me"

    def __init__(self, client_id, client_secret, redirect_uri, fields, scope):
        """
            Initialize the Facebook provider with client credentials.

            Args:
                client_id (str): The client ID provided by Facebook.
                client_secret (str): The client secret provided by Facebook.
                redirect_uri (str): The URI to redirect to after authentication.
        """
        super().__init__(client_id, client_secret, redirect_uri, fields, scope)

    def get_authorization_url(self, state=None, scope=None):
        """
        Generate the authorization URL to redirect the user for authentication.

        Args:
            state (str, optional): An unguessable random string to protect against CSRF attacks.

        Returns:
            str: The authorization URL.
            :param state: random string
            :param scope: the permissions the FB has
        """
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "response_type": "code",
            "scope": scope or self.scope,
        }

        if state:
            params["state"] = state
        return f"{self.AUTHORIZE_URL}?{urlencode(params)}"


    def get_access_token(self, code: str) -> str:
        """
        Exchange the authorization code for an access token.

        Args:
            code (str): The authorization code received from the callback.

        Returns:
            str: The access token.
        """
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri,
            "code": code,
        }
        response = requests.get(self.TOKEN_URL, params=payload)
        response.raise_for_status()
        return response.json().get("access_token")


    def get_user_profile(self, access_token: str, fields: str = "id,name,email,picture") -> dict:
        """
        Fetch user profile information from Facebook.

        Args:
            access_token (str): The access token for the user.
            fields (str): A comma-separated string of fields to retrieve. Defaults to "id,name,email,picture".

        Returns:
            dict: The user profile data.
        """
        params = {"access_token":access_token, "fields":fields,}
        response = requests.get(self.PROFILE_URL, params=params)
        response.raise_for_status()
        return response.json()

