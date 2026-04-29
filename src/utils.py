import json
import pathlib
from user import User
from typing import Optional
from constants import FOLLOWING_FILE, FOLLOWERS_FILE, JsonData


def load_json(filepath: pathlib.Path) -> Optional[JsonData]:
    """
    Loads and parses a JSON file from the local filesystem.

    Args:
        filepath (Path): A pathlib.Path object pointing to the JSON file.

    Returns:
        Optional[JsonData]: The parsed JSON structure (list or dict).
                           Returns None if the file does not exist.
    """

    # Check if the path exists and is a file
    if not filepath.exists():
        print(f"Error: File not found at '{filepath}'")
        return None

    # Open file in read mode with UTF-8 encoding
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def load_following_json() -> list[User]:
    """
    Parses the 'following.json' file from an official Instagram data export.

    Returns:
        list[User]: A list of User objects representing accounts the user follows.
    """

    following = load_json(FOLLOWING_FILE)

    # Return an empty list if file is missing or contains no data
    if not following or "relationships_following" not in following:
        return list()

    # If the file does not contain any people, return an emoty list
    if not following:
        return list()

    # Map the nested JSON structure to User objects
    return [
        User(
            user_name=entry["title"],
            profile_link=entry["string_list_data"][0]["href"],
        )
        for entry in following["relationships_following"]
    ]


def load_followers_json() -> list[User]:
    """
    Parses the 'followers_1.json' file from an official Instagram data export.

    Returns:
        list[User]: A list of User objects representing accounts that follow the user.
    """

    followers = load_json(FOLLOWERS_FILE)

    # Return an empty list if file is missing or contains no data
    if not followers:
        return list()

    # Map the nested JSON structure to User objects
    return [
        User(
            user_name=entry["string_list_data"][0]["value"],
            profile_link=entry["string_list_data"][0]["href"],
        )
        for entry in followers
    ]


def not_following_back(
    following_list: list[User], follower_list: list[User]
) -> list[User]:
    """
    Compares following and follower lists to identify "ghosts" (accounts that do not follow back).

    Args:
        following_list (list[User]): List of users you are following.
        follower_list (list[User]): List of users following you.

    Returns:
        list[User]: Users who are followed by you but do not follow you back.
    """

    # Create a set of follower names for O(1) lookup performance
    follower_names = {u.user_name for u in follower_list}

    # Filter out users from the following list who are not in the follower set
    return [user for user in following_list if user.user_name not in follower_names]
