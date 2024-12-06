try:
    from fastapi import FastAPI, Request, HTTPException
    from fastapi.responses import RedirectResponse
    from pydantic import BaseModel
    from typing import Optional
except ImportError as e:
    raise ImportError("FastAPI is not installed. Install it using 'pip install omni-authify[fastapi]'") from e

from omni_authify import Facebook

class OmniAuthifyFastAPI:
    def __init__(self, provider_name: str):
        """
        Retrieve provider settings from environment variables or FastAPI settings.
        :param provider_name: The name of the provider, such as facebook or Twitter.
        """
        from omni_authify import settings




