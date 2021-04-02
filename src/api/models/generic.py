"""
File contains generic models
"""
from typing import List

from pydantic import BaseModel


class Message(BaseModel):
    """
    Generic message model
    """

    msg: str


class Results(BaseModel):
    """
    Generic results model

    Contains a list of messages
    """

    detail: List[Message]
