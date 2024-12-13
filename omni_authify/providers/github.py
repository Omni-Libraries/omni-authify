from urllib.parse import urlencode

import requests

from .base import BaseOAuth2Provider


class GitHub(BaseOAuth2Provider):
    """
    GitHub OAuth2 provider.
    """

    AUTHORIZE_URL: str = "https://github.com/login/oauth/authorize"
    TOKEN_URL: str = "https://github.com/login/oauth/access_token"
    PROFILE_URL: str = "https://api.github.com/user"

    def __init__(self, client_id, client_secret, redirect_uri, scope):
        """
            Initialize the GitHub provider with client credentials.

            Args:
                client_id (str): The client ID provided by GitHub.
                client_secret (str): The client secret provided by GitHub.
                redirect_uri (str): The URI to redirect to after authentication.
        """
        super().__init__(client_id, client_secret, redirect_uri, fields=['id'], scope=scope)

    def get_authorization_url(self, state=None, scope=None):
        """
        Generate the authorization URL to redirect the user for authentication.

        Returns:
            str: The authorization URL.
            :param state: random string
            :param scope: the permissions your OAuth apps has
        """
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "response_type": "code", # ==== expires after 10 minutes ====
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
            "code":code,
        }
        headers = {"Accept": "application/json"}
        response = requests.post(self.TOKEN_URL, data=payload, headers=headers)
        response.raise_for_status()
        return response.json().get("access_token")

    def check_token_scopes(self, access_token):
        """
        Check the OAuth scopes for the given access token.

        Args:
            access_token (str): The OAuth access token to inspect.

        Returns:
            dict: A dictionary containing:
                - 'authorized_scopes': Scopes the token has been authorized with
                - 'accepted_scopes': Scopes accepted by the GitHub API
        """
        try:
            response = requests.head(
                self.PROFILE_URL, headers={'Authorization':f'Bearer {access_token}'}
            )
            response.raise_for_status()

            return {'authorized_scopes':response.headers.get('X-OAuth-Scopes', '').split(', '),
                'accepted_scopes':response.headers.get('X-Accepted-OAuth-Scopes', '').split(', ')}
        except requests.RequestException as e:
            return {'error':str(e), 'authorized_scopes':[], 'accepted_scopes':[]}


    def get_user_profile(self, access_token, scope=None):
        """
        Fetch user profile information from GitHub.

        Args:
            access_token (str): The access token for the user.
            scope (str): A comma-separated string of fields to retrieve. Defaults to "user,repo".

        Returns:
            dict: The user profile data.
        """
        headers = {"Authorization": f'Bearer {access_token}'}
        response = requests.get(self.PROFILE_URL, headers=headers)
        response.raise_for_status()
        return response.json()

