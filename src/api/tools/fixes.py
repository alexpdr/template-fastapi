"""
File contains various fixes and work-a-rounds
"""

from typing import Callable, List, Tuple

from fastapi import FastAPI


class Fixes:
    """
    Contains various fixes and work-a-rounds
    """

    @staticmethod
    def override_body_schema(
        app: FastAPI, function: Callable, name: str
    ) -> None:
        """
        Updates the Pydantic schema name for a FastAPI function that takes
        in a fastapi.UploadFile = File(...) or bytes = File(...).

        This is a known issue that was reported on FastAPI#1442 in which
        the schema for file upload routes were auto-generated with no
        customization options. This renames the auto-generated schema to
        something more useful and clear.

        Args:
            app: The FastAPI application to modify.
            function: The function object to modify.
            name: The new name of the schema.

        Examples:
            - name_schema(app, create_file, "CreateFileSchema")
            - name_schema(app, create_upload_file, "CreateUploadSchema")
        """
        for route in app.routes:
            if route.endpoint is function:
                route.body_field.type_.__name__ = name
                break

    @staticmethod
    def override_body_schemas(
        app: FastAPI, overrides: List[Tuple[Callable, str]]
    ) -> None:
        """
        Updates the Pydantic schema name for a FastAPI function that takes
        in a fastapi.UploadFile = File(...) or bytes = File(...).

        This is a known issue that was reported on FastAPI#1442 in which
        the schema for file upload routes were auto-generated with no
        customization options. This renames the auto-generated schema to
        something more useful and clear.

        Args:
            app: FastAPI, the fastapi instance to modify
            overrides: List[Tuple[Callable, str]], tuple of method, name to use

        Examples:
            - name_schema(app, create_file, "CreateFileSchema")
            - name_schema(app, create_upload_file, "CreateUploadSchema")

        """
        for route in app.routes:
            for entry in overrides:
                if route.endpoint is entry[0]:
                    route.body_field.type_.__name__ = entry[1]
                    break
