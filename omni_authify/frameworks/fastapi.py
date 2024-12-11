try:
    from fastapi import FastAPI, Request, HTTPException
    from fastapi.responses import RedirectResponse
    from pydantic import BaseModel
    from typing import Optional

    from ..core.utils import OMNI_AUTHIFY

except ImportError as e:
    raise ImportError("FastAPI is not installed. Install it using 'pip install omni-authify[fastapi]'") from e

from omni_authify import Facebook


class OmniAuthifyFastAPI:
    def __init__(self, provider_name):
        """
        Retrieve provider settings from environment variables or FastAPI settings.
        :param provider_name: The name of the provider, such as facebook or Twitter.
        """

        provider_settings = OMNI_AUTHIFY['PROVIDERS'].get(provider_name=provider_name)
        if not provider_settings:
            raise NotImplementedError(f"Provider settings for '{provider_name}' not found in OMNI_AUTHIFY settings.")

        self.provider_name = provider_name
        self.fields = provider_settings.get('fields')
        self.scope = provider_settings.get('scope')
        self.state = provider_settings.get('state')
        self.provider = self.get_provider(provider_name, provider_settings)

    def get_provider(self, provider_name, provider_settings):
        match provider_name:
            case 'facebook':
                return Facebook(
                    client_id=provider_settings.get('client_id'),
                    client_secret=provider_settings.get('client_secret'),
                    redirect_uri=provider_settings.get('redirect_uri'),
                    scope=provider_settings.get('scope'),
                    fields=provider_settings.get('fields'),
                )

            # case 'google':
            #     return Google(
            #
            #     )
            # case 'twitter':
            #     return twitter(
            #
            #     )
            #
            # # add other providers as they get ready
            case _:
                return f"Provider '{provider_name}' is not implemented."

    def get_auth_url(self, request, scope=None):
        """
        Generate the authorization URL
        :return:
        """
        scope = scope or self.scope
        return  self.provider.get_authorization_url(state=self.state, scope=scope)

    def get_user_info(self, request, code):
        """
        Exchange code for access token and fetch user profile
        :param request:
        :param code: code from the provider to get access token
        :return:
        """
        error = request.GET.get('error')
        if error:
            return {'error':True, 'message':f"Error: {error}", 'status':400}

        access_token = self.provider.get_access_token(code=code)
        user_info = self.provider.get_user_profile(access_token=access_token, fields=self.fields)
        return user_info




