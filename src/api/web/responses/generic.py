"""
File contains generic and shared responses
"""
from api.models.generic import Results


class Generic:
    """
    Class contains generic and shared responses
    """
    # 200s
    success = {
        "200":{
            "model": Results,
            "description": "Successfully processed operation"
        }
    }

    # 400s
    not_found = {
        "404": {
            "model": Results,
            "description": "Could not find requested resource",
        },
    }
    conflict = {
        "409": {
            "model": Results,
            "descriptions": "The requested resource already exists!",
        }
    }
    unprocessable = {
        "422": {
            "model": Results,
            "descriptions": "Server could not process entity",
        }
    }
    # 500s
    server_error = {
        "500": {
            "model": Results,
            "description": "Server could not process request",
        },
    }
