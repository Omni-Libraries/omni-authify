import requests

from urllib.parse import urlencode

from .base import BaseOAuth2Provider


class Google(BaseOAuth2Provider):
    """
    Google OAuth2 provider.
    """
    AUTHORIZE_URL: str = "https://accounts.google.com/o/oauth2/v2/auth"
    PROFILE_URL: str = "https://www.googleapis.com/oauth2/v1/userinfo"

    def __init__(self, client_id, client_secret, redirect_uri, scope="openid email profile"):
        """
            Initialize the Google provider with client credentials.

            Args:
                client_id (str): The client ID provided by Google.
                client_secret (str): The client secret provided by Google.
                redirect_uri (str): The URI to redirect to after authentication.
                scope (str, optional): The scope of access requested. Defaults to "openid email profile".
        """
        super().__init__(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope, fields=["id"])
        
        
    def get_authorization_url(self, state=None, scope=None):
        """ 
        Generate the authorization URL for Google OAuth2.

        Returns:
            str: The authorization URL. 
        """
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "response_type": "token",
            "scope": scope or self.scope,
        }
        if state:
            params["state"] = state
        return f"{self.AUTHORIZE_URL}?{urlencode(params)}"


    def get_access_token(self) -> str:
        return super().get_access_token()


    def get_user_profile(self, access_token: str) -> dict:
        """
        Fetch user profile information from Google.

        Args:
            access_token (str): The access token for the user.

        Returns:
            dict: The user profile data.
        """
        response = requests.get(f"{self.PROFILE_URL}?access_token={access_token}")
        response.raise_for_status()
        return response.json()