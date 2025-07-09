import os
import sys

application_environment = os.getenv("APP_ENV")

if application_environment == "test" or any("pytest" in arg for arg in sys.argv):

    db_connect_configuration = {
        "url": "sqlite:///temp.db",
        "connect_args": {"check_same_thread": False},
        "echo": True,
    }
elif application_environment == "production":
    try:
        db_connect_configuration = {
            "url": "postgresql+psycopg2://"
            + os.environ["DB_USER"]
            + ":"
            + os.environ["DB_PASSWORD"]
            + "@"
            + os.environ["DB_HOST"]
            + ":5432/"
            + os.environ["DB_NAME"]
        }
    except KeyError as e:
        raise KeyError(f"Variable {e.args[0]} must be specified")
else:
    raise ValueError("variable APP_ENV must be specified as test or production")
