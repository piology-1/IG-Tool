from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    """
    Represents an Instagram user account.

    Attributes:
        user_name (str): The unique Instagram handle (e.g., 'fcbayern').
        profile_link (str): The direct URL to the user's profile.

    Note:
        The class is marked as 'frozen=True' to ensure instances are immutable.
        This allows Python to generate a stable hash value, enabling User objects
        to be stored in sets or used in set-based comparisons.
    """

    user_name: str
    profile_link: str
