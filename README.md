# 🌳 The Listening Tree

A personalized music recommendation CLI app built in Python.  
Answer five simple questions and get a curated playlist tailored to your taste.

---

## 🚀 How to Run

```bash
cd the_listening_tree
python main.py
```

No dependencies required — pure Python 3.9+.

---

## 🎵 How It Works

The app walks you through five steps:

| Step | Question | Options |
|------|----------|---------|
| 1 | **Language** | English · Non-English · Hindi · Non-Hindi |
| 2 | **Genre** | Pop · Rock · Devotional · Classical · Jazz · Indie · Bollywood |
| 3 | **Style** | Acoustic · Electronic · Fusion · Lo-fi |
| 4 | **Time Period** | 1950–1970 · 1970–1990s · 1990–2010s · 2010–2020s |
| 5 | **Popularity** | Trending · Classics |

After all five choices, the app filters a curated database of 90+ songs and displays a personalized playlist of up to 6 tracks. If exact matches are too few, filters are relaxed gracefully to ensure you always get results.

---

## 📁 Project Structure

```
the_listening_tree/
├── main.py          # CLI wizard — entry point
├── recommender.py   # Filtering and recommendation logic
├── songs_data.py    # Curated song database (90+ songs)
└── README.md        # This file
```

---

## ✨ Features

- **Step-by-step wizard** with a progress bar
- **Coloured terminal output** using ANSI codes (no extra library needed)
- **Smart fallback** — if no exact match is found, filters relax automatically
- **Shuffled results** — different playlist each run for the same preferences
- **Play again** option after each recommendation

---

## 🧠 Design Decisions

- **No API keys or internet required** — songs are stored in a local Python dict
- **Zero third-party dependencies** — works out of the box with any Python 3.9+ install
- **Graceful degradation** — 6 fallback levels ensure you always get recommendations
- **Windows compatible** — ANSI colour mode is enabled at startup on Windows 10+

---

## 📌 Requirements

- Python 3.9 or higher

---

*Built with ❤️ as a portfolio project.*
