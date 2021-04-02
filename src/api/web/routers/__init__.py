"""
Module contains routers
"""
from typing import List
from fastapi import APIRouter

from .example import router as ExampleRouter

ROUTERS: List[APIRouter] = [
    ExampleRouter
]
