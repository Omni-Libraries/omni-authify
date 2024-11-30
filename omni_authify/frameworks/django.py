try:
    from django.conf import settings
    from django.contrib.auth import login
    from django.contrib.auth.models import User
    from django.http import HttpResponse, HttpResponseRedirect
    from django.shortcuts import redirect
except ImportError as e:
    raise ImportError("Django is not installed. Install it using 'pip install omni-authify[django]'") from e

from omni_authify import Facebook


class OmniAuthifyDjango:
    def __init__(self, provider_name):
        """
        Retrieves provider settings from Django settings
        :param provider_name:
        """
        home_page_settings = settings.OMNI_AUTHIFY['HOME_PAGE'].get('dashboard')
        self.home = home_page_settings.get('home')

        auto_authenticate = settings.OMNI_AUTHIFY['AUTO_AUTHENTICATE'].get('auth')
        self.auto_authenticate = auto_authenticate.get('authenticate')

        provider_settings = settings.OMNI_AUTHIFY['PROVIDERS'].get(provider_name)
        if not provider_settings:
            raise ValueError(f"Provider settings for '{provider_name}' not found in OMNI_AUTHIFY settings.")

        self.provider_name = provider_name
        self.fields = provider_settings.get('fields', 'id,name,email')  # Default fields if not set
        self.state = provider_settings.get('state')
        self.provider = self.get_provider(provider_name, provider_settings)

    def get_provider(self, provider_name, provider_settings):
        match provider_name:
            case 'facebook':
                return Facebook(
                    client_id=provider_settings.get('client_id'),
                    client_secret=provider_settings.get('client_secret'),
                    redirect_uri=provider_settings.get('redirect_uri'),
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

    def login(self, request) -> redirect:
        """
        Generates the authorization URL and redirects the user
        :return: url
        """
        auth_url = self.provider.get_authorization_url(state=self.state)
        return redirect(auth_url)

    def callback(self, request) -> HttpResponse | HttpResponseRedirect | dict:
        """
        Handles the callback from the provider, exchanges the code for an access token, fetches user info,
        and authenticates the user.
        :param request:
        :return: HttpResponse
        """
        error = request.GET.get('error')
        if error:
            return HttpResponse(f"Error: {error}", status=400)

        code = request.GET.get('code')
        if not code:
            return HttpResponse(f"No code provided", status=400)

        try:
            access_token = self.provider.get_access_token(code=code)
            user_info = self.provider.get_user_profile(access_token=access_token, fields=self.fields)
            return user_info
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}", status=500)
