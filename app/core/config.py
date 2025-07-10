import os
import sys

if any("pytest" in arg for arg in sys.argv):
    os.environ["APP_ENV"] = "test"

application_environment = os.getenv("APP_ENV")

if application_environment == "test":
    os.environ["APP_ENV"] = "test"
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
            + "@db:5432/"
            + os.environ["DB_NAME"]
        }
    except KeyError as e:
        raise KeyError(f"Variable {e.args[0]} must be specified")
else:
    raise ValueError("variable APP_ENV must be specified as test or production")
