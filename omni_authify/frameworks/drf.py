try:
    from django.conf import settings
    from django.contrib.auth.models import User
    from rest_framework import status
    from rest_framework.response import Response
    from rest_framework.views import APIView
except ImportError as e:
    raise ImportError("Django Rest Framework is not installed. Install it using 'pip install omni-authify[drf]'") \
        from e

from omni_authify import Facebook


class OmniAuthifyDRF:
    def __init__(self, provider_name):
        """
        Retrieve provider settings from Django settings
        :param provider_name: The name of the provider such as Facebook or Twitter
        """
        home_page_settings = settings.OMNI_AUTHIFY['HOME_PAGE'].get('dashboard')
        self.home = home_page_settings.get('home')

        provider_settings = settings.OMNI_AUTHIFY['PROVIDERS'].get(provider_name=provider_name)
        if not provider_settings:
            raise NotImplementedError(f"Provider settings for '{provider_name}' not found in OMNI_AUTHIFY settings.")

        self.provider_name = provider_name
        self.fields = provider_settings.get('fields')
        self.state = provider_settings.get('state')
        self.provider = self.get_provider(provider_name, provider_settings)

    def get_provider(self, provider_name, provider_settings):
        if provider_name == 'facebook':
            return Facebook(
                client_id=provider_settings.get('client_id'),
                client_secret=provider_settings.get('client_secret'),
                redirect_uri=provider_settings.get('redirect_uri'),
            )

        # elif provider_name == 'twitter':
        # elif provider_name == 'google':

        else:
            raise NotImplementedError(f"Provider '{provider_name}' is not implemented.")

    def get_auth_url(self):
        """
        Generate the authorization URL
        :return:
        """
        return  self.provider.get_authorization_url(state=self.state)

    def get_user_info(self, code):
        """
        Exchange code for access token and fetch user profile
        :param code: code from the provider to get access token
        :return:
        """
        access_token = self.provider.get_access_token(code=code)
        user_info = self.provider.get_user_profile(access_token=access_token, fields=self.fields)
        return user_info




