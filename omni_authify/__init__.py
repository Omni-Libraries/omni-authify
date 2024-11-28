from .providers.facebook import Facebook
from .providers.instagram import Instagram

# Commented out providers not yet implemented
# from .providers.linkedin import LinkedIn
# from .providers.google import Google
# from .providers.twitter import Twitter
# from .providers.github import GitHub
#
from .frameworks.django import OmniAuthifyDjango
from .frameworks.django_drf import OmniAuthifyDRF
# from .frameworks.flask import FlaskAuth
# from .frameworks.fastapi import FastAPIAuth


__all__ = [
    "Facebook",
    "Instagram",
    # Other providers can be added once implemented
    # "LinkedIn",
    # "Telegram",
    # "Twitter",
    # "Google",
    # "GitHub",

    "OmniAuthifyDjango",
    "OmniAuthifyDRF",
]

__version__ = "0.1.0"
