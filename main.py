"""
main.py — The Listening Tree
A step-by-step CLI music recommendation app with YouTube playback.
"""

import sys
from recommender import recommend
from youtube_helper import open_song

# ── ANSI colour helpers (Windows 10+ and all Unix terminals) ────────────────

RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
GREEN   = "\033[32m"
CYAN    = "\033[36m"
YELLOW  = "\033[33m"
MAGENTA = "\033[35m"
WHITE   = "\033[97m"
BLUE    = "\033[34m"


def c(text: str, colour: str) -> str:
    return f"{colour}{text}{RESET}"


# ── ASCII art welcome banner ────────────────────────────────────────────────

BANNER = rf"""
{CYAN}{BOLD}
  ████████╗██╗  ██╗███████╗
  ╚══██╔══╝██║  ██║██╔════╝
     ██║   ███████║█████╗
     ██║   ██╔══██║██╔══╝
     ██║   ██║  ██║███████╗
     ╚═╝   ╚═╝  ╚═╝╚══════╝
{RESET}
{MAGENTA}{BOLD}   🌳  L I S T E N I N G   T R E E  🌳{RESET}
{DIM}   Your personal music recommendation guide{RESET}
"""


# ── Menu helpers ────────────────────────────────────────────────────────────

def print_step(step: int, total: int, title: str) -> None:
    bar_filled = "█" * step
    bar_empty  = "░" * (total - step)
    print(f"\n{DIM}  Step {step}/{total}  {bar_filled}{bar_empty}{RESET}")
    print(f"  {CYAN}{BOLD}{title}{RESET}")
    print(f"  {DIM}{'─' * 40}{RESET}")


def show_menu(options: list[str]) -> None:
    for i, opt in enumerate(options, 1):
        print(f"  {YELLOW}{BOLD}[{i}]{RESET}  {opt}")


def get_choice(options: list[str]) -> str:
    while True:
        try:
            raw = input(f"\n  {GREEN}▶  Enter choice (1–{len(options)}): {RESET}").strip()
            idx = int(raw) - 1
            if 0 <= idx < len(options):
                return options[idx]
            print(f"  {YELLOW}Please enter a number between 1 and {len(options)}.{RESET}")
        except ValueError:
            print(f"  {YELLOW}Invalid input. Please enter a number.{RESET}")
        except EOFError:
            print()
            sys.exit(0)


def ask_replay() -> bool:
    while True:
        try:
            raw = input(f"\n  {GREEN}▶  Play again? (y/n): {RESET}").strip().lower()
            if raw in ("y", "yes"):
                return True
            if raw in ("n", "no"):
                return False
            print(f"  {YELLOW}Please type y or n.{RESET}")
        except EOFError:
            return False


# ── Results display ─────────────────────────────────────────────────────────

def display_results(songs: list[dict], relaxed: bool, prefs: dict) -> None:
    print(f"\n  {DIM}{'═' * 52}{RESET}")
    print(f"  {MAGENTA}{BOLD}🎵  Your Personalised Playlist{RESET}")
    print(f"  {DIM}{'═' * 52}{RESET}")

    tags = [c(prefs[k], CYAN) for k in ("language", "genre", "style", "era", "popularity")]
    print(f"\n  {DIM}Filters:{RESET}  {' · '.join(tags)}")

    if relaxed:
        print(f"\n  {YELLOW}⚡  Not enough exact matches — showing best alternatives.{RESET}")

    print()
    for i, song in enumerate(songs, 1):
        num    = c(f"  {i:>2}.", DIM)
        title  = c(song["title"], f"{WHITE}{BOLD}")
        artist = c(song["artist"], MAGENTA)
        meta   = c(f"[{song['genre']} · {song['style']} · {song['era']}]", DIM)
        print(f"{num}  {title}")
        print(f"      {artist}  {meta}")
        print()

    print(f"  {DIM}{'─' * 52}{RESET}")


# ── YouTube play flow ───────────────────────────────────────────────────────

def play_menu(songs: list[dict]) -> None:
    """
    Let the user pick any song to open on YouTube in their default browser.
    They can open multiple songs one after another, or type 0 to skip.
    """
    print(f"\n  {CYAN}{BOLD}🎧  Open a song on YouTube?{RESET}")
    print(f"  {DIM}{'─' * 52}{RESET}")

    for i, song in enumerate(songs, 1):
        label = c(f"  [{i}]", YELLOW + BOLD)
        title  = c(song["title"], WHITE + BOLD)
        artist = c(song["artist"], MAGENTA)
        print(f"{label}  {title}  —  {artist}")

    skip_label = c("  [0]", DIM)
    print(f"{skip_label}  {c('Skip / done', DIM)}")

    while True:
        try:
            raw = input(f"\n  {GREEN}▶  Enter song number (0 to skip): {RESET}").strip()
            idx = int(raw)
            if idx == 0:
                return
            if 1 <= idx <= len(songs):
                song = songs[idx - 1]
                _open_on_youtube(song)
            else:
                print(f"  {YELLOW}Please enter a number between 0 and {len(songs)}.{RESET}")
        except ValueError:
            print(f"  {YELLOW}Invalid input.{RESET}")
        except EOFError:
            return


def _open_on_youtube(song: dict) -> None:
    title  = song["title"]
    artist = song["artist"]
    print(f"\n  {DIM}Searching YouTube for  {RESET}{c(title, WHITE + BOLD)}  {c('—', DIM)}  {c(artist, MAGENTA)}", end="", flush=True)

    url, is_direct = open_song(title, artist)

    if is_direct:
        status = c("✔ direct link found", GREEN)
    else:
        status = c("⚡ showing search results (offline or first visit)", YELLOW)

    print(f"\r  {status}{' ' * 10}")
    print(f"  {BLUE}🔗  {url}{RESET}")
    print(f"  {DIM}Opening in your browser...{RESET}")


# ── Main wizard flow ─────────────────────────────────────────────────────────

TOTAL_STEPS = 5

STEPS = [
    {
        "key":     "language",
        "title":   "Select Language",
        "options": ["English", "Non-English", "Hindi", "Non-Hindi"],
    },
    {
        "key":     "genre",
        "title":   "Choose Genre",
        "options": ["Pop", "Rock", "Devotional", "Classical", "Jazz", "Indie", "Bollywood"],
    },
    {
        "key":     "style",
        "title":   "Pick Style",
        "options": ["Acoustic", "Electronic", "Fusion", "Lo-fi"],
    },
    {
        "key":     "era",
        "title":   "Select Time Period",
        "options": ["1950-1970", "1970-1990s", "1990-2010s", "2010-2020s"],
    },
    {
        "key":     "popularity",
        "title":   "Popularity Preference",
        "options": ["Trending", "Classics"],
    },
]


def run_wizard() -> None:
    prefs: dict[str, str] = {}

    for step_num, step in enumerate(STEPS, 1):
        print_step(step_num, TOTAL_STEPS, step["title"])
        show_menu(step["options"])
        prefs[step["key"]] = get_choice(step["options"])
        print(f"\n  ✔  Selected: {c(prefs[step['key']], GREEN + BOLD)}")

    print(f"\n  {DIM}Finding your songs...{RESET}", end="", flush=True)
    songs, relaxed = recommend(**prefs)
    print(f"\r{' ' * 40}\r", end="")

    display_results(songs, relaxed, prefs)
    play_menu(songs)
    print(f"\n  {DIM}Enjoy listening! 🎧{RESET}")


def main() -> None:
    if sys.platform == "win32":
        import os
        os.system("")   # enable VT100 / ANSI on Windows console

    print(BANNER)

    while True:
        run_wizard()
        if not ask_replay():
            print(f"\n  {CYAN}Thank you for using The Listening Tree! 🌳{RESET}\n")
            break
        print(f"\n  {DIM}Starting over...{RESET}")


if __name__ == "__main__":
    main()
