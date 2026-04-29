import pathlib
from typing import Any, Union

# Path to the project's root directory (old: os.path.join)
BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent
DATA_FOLDER: pathlib.Path = BASE_DIR / "data"

# This is the JSON file containing the people you are following
FOLLOWING_FILE: pathlib.Path = DATA_FOLDER / "following.json"

# This is the JSON file that contains the people who are following you
FOLLOWERS_FILE: pathlib.Path = DATA_FOLDER / "followers_1.json"


# Defining a type for JSON data (dictionary or list)
JsonData = Union[dict[str, Any], list[Any]]
