"""
File ontains responses for the example router
"""
from api.models import Example

from .generic import Generic


class Example:
    """
    Wrapper class containing example router responses
    """

    placeholder = {
        "200": {
            "model": Example,
            "description": "Downloads and returns the file",
        },
        **Generic.not_found,
        **Generic.server_error,
    }
