import os
import sys
from typing import Any

if any("pytest" in arg for arg in sys.argv):
    os.environ["APP_ENV"] = "test"

application_environment = os.getenv("APP_ENV")


def get_db_configuration() -> dict[str, Any]:

    if application_environment == "test":
        return {
            "url": "sqlite:///temp.db",
            "connect_args": {"check_same_thread": False},
            "echo": True,
        }
    elif application_environment == "production":
        try:
            return {
                "url": "postgresql+psycopg2://"
                + os.environ["DB_USER"]
                + ":"
                + os.environ["DB_PASSWORD"]
                + "@db:5432/"
                + os.environ["DB_NAME"]
            }
        except KeyError as e:
            raise KeyError(f"Variable {e.args[0]} must be specified")
    else:
        raise ValueError("variable APP_ENV must be specified as test or production")


db_connect_configuration = get_db_configuration()
