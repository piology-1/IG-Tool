from utils import load_following_json, load_followers_json, not_following_back
from user import User


def main():
    """
    Main entry point of the application
    """

    # Get a list of user objects for the following and followers JSON files
    following_data: list[User] = load_following_json()
    followers_data: list[User] = load_followers_json()

    # First feature: Get a list of users, who are not following back
    not_back: list[User] = not_following_back(
        following_list=following_data, follower_list=followers_data
    )

    ###
    # Print the results in a pretty format
    ###

    # Header
    title = " USERS NOT FOLLOWING BACK "
    print(f"\n{title:=^100}")  # Centers the title between '=' characters
    print(f"{'Username':<40} | {'Profile Link'}")
    print("-" * 100)

    for user in not_back:
        # :<40 ensures that the name always takes up 40 characters
        print(f"{user.user_name:<40} | {user.profile_link}")

    # Footer
    print("-" * 100)
    print(f"TOTAL: {len(not_back)} Ghosts found")
    print(f"{'='*100}\n")


if __name__ == "__main__":
    main()
