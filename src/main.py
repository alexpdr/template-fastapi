"""
Main Application file

Used as target when running the ASGI server
ex: `uvicorn main:app --reload`
"""
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from api.web import Web
from api.settings import SETTINGS


# Initialize application with settings
app = FastAPI(**SETTINGS["app"])

# Add the routers
[app.include_router(router) for router in Web.Routers]

# Add the middleware
[app.include_router(middleware) for middleware in Web.Middleware]

# Root/Index response
@app.get(
    path="/",
    operation_id="api.index",
    tags=["System"],
)
async def index():
    """
    API Index, returns redirect to docs
    """
    return RedirectResponse("/docs")
