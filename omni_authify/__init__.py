from .providers.facebook import Facebook
from .providers.instagram import Instagram
from .providers.github import GitHub
from .providers.google import Google

# Commented out providers not yet implemented
# from .providers.linkedin import LinkedIn
# from .providers.twitter import Twitter


__all__ = [
    "Facebook",
    "Instagram",
    "GitHub",
    "Google",

    # Other providers will be added once implemented
    # "LinkedIn",
    # "Telegram",
    # "Twitter",
]

__version__ = "1.1.7"

