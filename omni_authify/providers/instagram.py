import requests

from .facebook import Facebook


class Instagram(Facebook):
    """
    Instagram currently not supported.
    """
    PROFILE_URL: str = "https://graph.instagram.com/me"

    def get_user_profile(self, access_token: str, fields: str) -> dict:
        payload = {
            "access_token": access_token,
            "fields": fields,
        }
        response = requests.get(self.PROFILE_URL, params=payload)
        response.raise_for_status()
        return response.json()

