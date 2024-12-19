from omni_authify import Facebook, GitHub, Google

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

        #     )
        # case 'twitter':
        #     return twitter(
        #
        #     )
        #
        # # add other providers as they get ready
        case _:
            raise NotImplementedError(f"Provider '{provider_name}' is not implemented.")
