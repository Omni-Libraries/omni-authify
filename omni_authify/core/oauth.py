from omni_authify import Facebook, GitHub, Google
from omni_authify.providers.linkedin import LinkedIn


def get_provider(provider_name, provider_settings):
    match provider_name:
        case 'facebook':
            return Facebook(
                client_id=provider_settings.get('client_id'),
                client_secret=provider_settings.get('client_secret'),
                redirect_uri=provider_settings.get('redirect_uri'),
                scope=provider_settings.get('scope'),
                fields=provider_settings.get('fields'),
            )
        case 'github':
            return GitHub(
                client_id=provider_settings.get('client_id'),
                client_secret=provider_settings.get('client_secret'),
                redirect_uri=provider_settings.get('redirect_uri'),
                scope=provider_settings.get('scope'),
            )
        case 'google':
                return Google(
                    client_id=provider_settings.get('client_id'),
                    client_secret=provider_settings.get('client_secret'),
                    redirect_uri=provider_settings.get('redirect_uri'),
                    scope=provider_settings.get('scopes'),
                )
        case 'linkedin':
            return LinkedIn(
                client_id=provider_settings.get('client_id'),
                client_secret=provider_settings.get('client_secret'),
                redirect_uri=provider_settings.get('redirect_uri'),
                scope=provider_settings.get('scope'),
            )

        #     )
        # case 'twitter':
        #     return twitter(
        #     )

        case _:
            raise NotImplementedError(f"Provider '{provider_name}' is not implemented.")
