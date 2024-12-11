import abc


class BaseOAuth2Provider(abc.ABC):
    def __init__(self, client_id, client_secret, redirect_uri, fields, scope):

        # ======== Validate input parameters ========
        assert client_id, "FACEBOOK_CLIENT_ID must be provided"
        assert client_secret, "FACEBOOK_CLIENT_SECRET must be provided"
        assert redirect_uri, "FACEBOOK_REDIRECT_URI must be provided"
        assert scope, "FACEBOOK_SCOPE must be provided"
        assert fields, "FACEBOOK_FIELDS must be provided"

        # ======== Assign input params to the instance variables ========
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.fields = fields or []
        self.scope = scope

    @abc.abstractmethod
    def get_authorization_url(self, state=None, scope=None):
        pass

    @abc.abstractmethod
    def get_access_token(self, code):
        pass

    @abc.abstractmethod
    def get_user_profile(self, access_token, fields=None):
        pass




