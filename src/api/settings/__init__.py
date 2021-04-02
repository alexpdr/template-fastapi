"""
Module contains application settings
"""
import json
from logging import getLogger
from pathlib import Path

SETTINGS: dict = {}
logger = getLogger(__name__)

# Load each settings file
for file in Path("api/settings").absolute().iterdir():
    if (
        file.name.startswith("dist")
        or file.name.endswith(".py")
        or Path(file).is_dir()
    ):
        continue
    try:
        with open(file, "r") as config:
            SETTINGS[str(file.name).split(".")[0].lower()] = json.load(config)
    except json.decoder.JSONDecodeError:
        logger.warning(f"Could not decode settings:'{file.name}'")
