

class AuthifyException(Exception):
    """Base exception for Omni-Authify errors."""

class ProviderError(AuthifyException):
    """Exception raised for errors related to OAuth providers."""

class IntegrationError(AuthifyException):
    """Exception raised for integration errors."""
