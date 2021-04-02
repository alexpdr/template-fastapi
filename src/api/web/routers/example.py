"""
File contains endpoint routerController for /files
"""
from logging import getLogger
from typing import Optional

from fastapi import APIRouter, HTTPException, Path
from fastapi.responses import Response

from api.web.responses import Responses
from api.models import Example
from api.settings import SETTINGS

logger = getLogger(__name__)
router = APIRouter(
    prefix="/example",
    tags=["Examples"],
)

@router.post(
    path="/",
    operation_id="api.http.routers.files.lookup",
    responses=Responses.Example.placeholder,
    response_model=Example
)
async def example_placeholder(example: Example):
    """
    Example endpoint
    """
    return example
