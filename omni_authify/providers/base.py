import abc


class BaseOAuth2Provider(abc.ABC):
    def __init__(self, client_id, client_secret, redirect_uri, fields, scope):

        # ======== Validate input parameters ========
        assert client_id, "CLIENT_ID must be provided"
        assert client_secret, "CLIENT_SECRET must be provided"
        assert redirect_uri, "REDIRECT_URI must be provided"
        assert scope, "SCOPE must be provided"
        assert fields, "FIELDS must be provided"

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




