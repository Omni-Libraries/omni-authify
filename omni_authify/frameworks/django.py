from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect

from omni_authify import Facebook


class OmniAuthifyDjango:
    def __init__(self, provider_name):
        """
        Retrieves provider settings from Django settings
        :param provider_name:
        """
        home_page_settings = settings.OMNI_AUTHIFY['HOME_PAGE'].get('dashboard')

        self.home = home_page_settings.get('home')

        provider_settings = settings.OMNI_AUTHIFY['PROVIDERS'].get(provider_name)
        if not provider_settings:
            raise ValueError(f"Provider settings for '{provider_name}' not found in OMNI_AUTHIFY settings.")

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

    def login(self, request) -> redirect:
        """
        Generates the authorization URL and redirects the user
        :return: url
        """
        auth_url = self.provider.get_authorization_url(state=self.state)
        return redirect(auth_url)

    def callback(self, request) -> HttpResponse:
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
            return HttpResponse(f"No code provided: {error}", status=400)

        try:
            access_token = self.provider.get_access_token(code=code)
            user_info = self.provider.get_user_profile(access_token=access_token, fields=self.fields)

            # ==== Authenticate and log in the user ====
            self.authenticate_user(user_info, request=request)
            return redirect(self.home)
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}", status=500)


    def authenticate_user(self, user_info, request) -> User:
        """
        Creates or retrieves a Django User object and logs in the user.
        :param user_info: User info fields from the Provider
        :param request:
        :return: User
        """
        # user, created = User.objects.get_or_create(
        #     username=f"{self.provider_name}_{user_info['id']}",
        #     defaults={
        #         'first_name':user_info.get('name', '').split(' ')[0],
        #         'last_name':' '.join(user_info.get('name', '').split(' ')[1:]),
        #         'email':user_info.get('email', '')}
        # )
        # login(request, user)
        # return user











