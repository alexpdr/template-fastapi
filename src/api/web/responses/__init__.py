"""
Module contains responses
"""
from dataclasses import dataclass
from .generic import Generic
from .example import Example


@dataclass
class Responses:
    """
    Response container class
    """
    Generic: Generic = Generic
    Example: Example = Example
