"""
File contains example model
"""
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class Example(BaseModel):
    """
    Example model
    """
    id: int
    created: datetime = Field(datetime.now())
    extra_values: Optional[List[str]]
