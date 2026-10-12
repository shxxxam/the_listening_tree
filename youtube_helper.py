"""
youtube_helper.py — YouTube link fetcher for The Listening Tree.

Online mode  : Scrapes a direct watch URL (youtube.com/watch?v=...) from
               YouTube search results — no API key, no extra libraries.
Offline mode : Falls back to a YouTube search URL so the user can still
               open YouTube and find the song manually.
"""

import re
import webbrowser
import urllib.parse


def _build_search_url(title: str, artist: str) -> str:
    """Construct a YouTube search URL for a given song."""
    query = urllib.parse.quote_plus(f"{title} {artist} official audio")
    return f"https://www.youtube.com/results?search_query={query}"


def get_youtube_url(title: str, artist: str) -> tuple[str, bool]:
    """
    Try to resolve a direct YouTube watch URL for the given song.

    Returns:
        (url, is_direct)
        - url       : Direct watch URL if found, otherwise a search URL
        - is_direct : True = direct video link, False = search results page
    """
    try:
        import requests

        query = urllib.parse.quote_plus(f"{title} {artist} official audio")
        search_url = f"https://www.youtube.com/results?search_query={query}"

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        }

        resp = requests.get(search_url, headers=headers, timeout=6)
        resp.raise_for_status()

        # YouTube embeds video IDs inside a JSON blob in the page source.
        # We grab the first one — it's almost always the top search result.
        video_ids = re.findall(r'"videoId"\s*:\s*"([a-zA-Z0-9_-]{11})"', resp.text)

        if video_ids:
            direct_url = f"https://www.youtube.com/watch?v={video_ids[0]}"
            return direct_url, True

    except Exception:
        pass  # network down, requests not installed, or YouTube changed layout

    # Fallback: search URL (still opens YouTube with the right query)
    return _build_search_url(title, artist), False


def open_song(title: str, artist: str) -> tuple[str, bool]:
    """
    Fetch the best URL for a song and open it in the default browser.

    Returns (url, is_direct) so the caller can inform the user.
    """
    url, is_direct = get_youtube_url(title, artist)
    webbrowser.open(url)
    return url, is_direct
