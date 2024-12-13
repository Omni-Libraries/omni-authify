try:
    from typing import Dict, Set, Tuple
    from django.conf import settings
    from django.contrib.auth import login
    from django.contrib.auth.models import User
    from django.http import HttpResponseRedirect
    from django.shortcuts import redirect
except ImportError as e:
    raise ImportError("Django is not installed. Install it using 'pip install omni-authify[django]'") from e

from omni_authify.core.oauth import get_provider


class OmniAuthifyDjango:
    def __init__(self, provider_name):
        """
        Retrieves provider settings from Django settings for authentication.
        :param provider_name: facebook, github,
        """
        provider_settings = settings.OMNI_AUTHIFY['PROVIDERS'].get(provider_name)
        if not provider_settings:
            raise ValueError(f"Provider settings for '{provider_name}' not found in OMNI_AUTHIFY settings.")

        self.provider_name = provider_name
        self.fields = provider_settings.get('fields')
        self.scope = provider_settings.get('scope')
        self.state = provider_settings.get('state')
        self.provider = get_provider(provider_name, provider_settings)

    def login(self, scope=None) -> redirect:
        """
        Generates the authorization URL and redirects the user
        """
        scope = scope or self.scope
        auth_url = self.provider.get_authorization_url(state=self.state, scope=scope)
        return redirect(auth_url)


    def callback(self, request) -> dict[str, bool | str | int] | tuple[dict, int] | dict[str, bool | str | int]:
        """
        Handles the callback from the provider, exchanges the code for an access token, fetches user info,
        and authenticates the user.
        :param request:
        :return: HttpResponse
        """
        error = request.GET.get('error')
        if error:
            return {'error':True, 'message':f"Error: {error}", 'status':400}

        code = request.GET.get('code')
        if not code:
            raise ValueError(f"No code provided")

        try:
            access_token = self.provider.get_access_token(code=code)
            user_info = self.provider.get_user_profile(access_token=access_token, fields=self.fields)
            return user_info, 200
        except Exception as e:
            return {'error':True, 'message':f"Error: {e}", 'status':500, }

