"""
File contains a generic log manager class
"""

import logging
from typing import List
from api.settings import SETTINGS

_SETTINGS = SETTINGS["logging"]


class LogManager:
    """
    Generic Log Manager to filter and clean log outputs
    """

    level: int
    overrides: List[str]

    def __init__(self):
        self.level = _SETTINGS["level"]
        self.overrides = _SETTINGS['overrides']

        if _SETTINGS["override_module_loggers"]:
            for module in self.blocked:
                self.override_module_logger(
                    module=module,
                    level=self.level
                )
        else:
            self.set_global_defaults(self.level)

    @staticmethod
    def override_module_logger(module: List[str], level: int):
        """
        Sets module log configurations
        """
        logging.getLogger(module).setLevel(level)

    @staticmethod
    def set_global_defaults(level: int):
        """
        Sets global log configuration
        """
        logging.basicConfig(level=level)
