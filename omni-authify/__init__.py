# omni_authify/__init__.py

from .providers.facebook import Facebook
from .providers.instagram import Instagram
from .providers.linkedin import LinkedIn
from .providers.google import Google
from .providers.twitter import Twitter
from .providers.github import GitHub

# Optionally, define __all__ for explicit export
__all__ = [
    'Facebook',
    'Instagram',
    'LinkedIn',
    'Google',
    'Twitter',
    'GitHub',
]