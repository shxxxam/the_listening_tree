"""
recommender.py — Recommendation engine for The Listening Tree.

Takes a user's preferences and returns a filtered list of songs.
Falls back gracefully when exact matches are too few.
"""

import random
from songs_data import SONGS


# ── Language mapping ────────────────────────────────────────────────────────

LANGUAGE_FILTER = {
    "English":     lambda lang: lang == "English",
    "Non-English": lambda lang: lang != "English",
    "Hindi":       lambda lang: lang == "Hindi",
    "Non-Hindi":   lambda lang: lang != "Hindi",
}


# ── Core recommendation logic ───────────────────────────────────────────────

def recommend(language: str, genre: str, style: str, era: str, popularity: str,
              max_results: int = 6) -> tuple[list[dict], bool]:
    """
    Filter songs by all five preferences and return up to max_results songs.

    Returns:
        (songs, relaxed)
        - songs   : list of matching song dicts
        - relaxed : True if some filters were relaxed to find results
    """
    lang_check = LANGUAGE_FILTER.get(language, lambda _: True)

    # ── Step 1: Try exact match on all 5 filters ────────────────────────────
    exact = [
        s for s in SONGS
        if lang_check(s["language"])
        and s["genre"] == genre
        and s["style"] == style
        and s["era"] == era
        and s["popularity"] == popularity
    ]
    if len(exact) >= 2:
        return _pick(exact, max_results), False

    # ── Step 2: Relax popularity ────────────────────────────────────────────
    relaxed_pop = [
        s for s in SONGS
        if lang_check(s["language"])
        and s["genre"] == genre
        and s["style"] == style
        and s["era"] == era
    ]
    if len(relaxed_pop) >= 2:
        return _pick(relaxed_pop, max_results), True

    # ── Step 3: Relax era ───────────────────────────────────────────────────
    relaxed_era = [
        s for s in SONGS
        if lang_check(s["language"])
        and s["genre"] == genre
        and s["style"] == style
    ]
    if len(relaxed_era) >= 2:
        return _pick(relaxed_era, max_results), True

    # ── Step 4: Relax style ─────────────────────────────────────────────────
    relaxed_style = [
        s for s in SONGS
        if lang_check(s["language"])
        and s["genre"] == genre
    ]
    if len(relaxed_style) >= 2:
        return _pick(relaxed_style, max_results), True

    # ── Step 5: Language + popularity only ─────────────────────────────────
    broad = [
        s for s in SONGS
        if lang_check(s["language"])
        and s["popularity"] == popularity
    ]
    if broad:
        return _pick(broad, max_results), True

    # ── Step 6: Just language ───────────────────────────────────────────────
    any_lang = [s for s in SONGS if lang_check(s["language"])]
    return _pick(any_lang, max_results), True


def _pick(songs: list[dict], n: int) -> list[dict]:
    """Return up to n songs, shuffled for variety."""
    pool = songs[:]
    random.shuffle(pool)
    return pool[:n]
