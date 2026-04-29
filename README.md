# Instagram-Analyzer

This is a lightweight, privacy-focused Python tool that can analyze Instagram data, such as the follower-to-following ratio, without requiring you to share your credentials. All you need to do is manually export the data using Instagram's built-in functionalities, and then let this tool work its magic on the data.

This tool only provides data analysis. It does not perform actions such as unfollowing or allow you to perform actions directly on your account. If you want to take action after reviewing the results, you need to go to Instagram and do so manually!

## Why this tool?

Most Instagram analyzer apps require your login information and only offer limited free options. Sometimes, all you want to know is basic information, and that's where this tool comes in!

==> TODO...

## Getting started

This project uses **uv** for dependency management.

```bash
# Clone the repository
git clone https://github.com/piology-1/IG-Tool
cd IG-Tool

# Install dependencies
uv sync
```

Run the analysis:

```bash
uv run .\src\main.py
```

## How to get your data

The project includes an example `following.json` and `followers_1.json` for demonstration purposes. To analyze your own account, follow these steps to export your data from Instagram:

==> TODO...

> [!IMPORTANT]  
> You must extract the downloaded directory and place the `.json` files directly into the `data/` folder so the tool can find them!

## Features

- List people who don't follow you back
- ...

## Future improvements

In the future, maybe a look at the [Instagram API](https://developers.facebook.com/docs/instagram-platform) could be interessting.

## License & Disclaimer

This tool is for educational purposes only. It is not affiliated with, authorized, maintained, sponsored, or endorsed by Instagram or Meta.
