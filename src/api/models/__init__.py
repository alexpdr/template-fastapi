"""
Module contains application models
"""
from dataclasses import dataclass
from .generic import Results, Message
from .example import Example


@dataclass
class Models:
    """
    Container class holding application models
    """
    Results: Results = Results
    Message: Message = Message
    Example: Example = Example
