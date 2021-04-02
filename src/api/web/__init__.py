"""
Module contains web sub-modules
"""
from .middleware import MIDDLEWARE
from .routers import ROUTERS

class Web:
    """
    Container class holding various web components
    """
    Middleware = MIDDLEWARE
    Routers = ROUTERS