## REQUIRMENTS

- **Python 3.7 or higher**

Check your version with:

python3 --version

If Python is not installed, download it from: https://www.python.org/downloads/


## HOW TO RUN

**1. Download or clone the project files into a folder:**

Devweekend-Fellowship/
  main.py
  db.py
  README.md

**2. Open a terminal and navigate into that folder:**

cd path/to/Devweekend-Fellowship


**3. Run the app:**

py main.py OR python3 main.py


**And it is done!** The app creates `app.db` automatically on first run.
No setup steps, no configuration, no extra installs.


## Example Terminal Session

  Welcome to Flashcard Study App!

  +------------------------------------------------+
  |         Flashcard Study App                    |
  +------------------------------------------------+
  |  1.  Add flashcard                             |
  |  2.  View all flashcards                       |
  |  3.  Update flashcard                          |
  |  4.  Delete flashcard                          |
  |  5.  Search flashcards                         |
  |  6.  Review random flashcard                   |
  |  7.  Exit                                      |
  +------------------------------------------------+

  Choose an option (1-7): 1

  ── ADD FLASHCARD ──
  ──────────────────────────────────────────────
  Title   : What is RAM?
  Content : Random Access Memory — temporary storage used by running programs.
  Tag     : (press Enter to skip) CS101

Flashcard saved!


  Choose an option (1-7): 6

  ── RANDOM REVIEW ──
  ──────────────────────────────────────────────

  Here is your random flashcard:

  ──────────────────────────────────────────────
  ID      : 1
  Title   : What is RAM?
  Content : Random Access Memory — temporary storage used by running programs.
  Tag     : CS101
  Created : 2025-01-15 14:30:00
  ──────────────────────────────────────────────


  Choose an option (1-7): 7

  Goodbye! Keep studying!


## How Persistence Works

When the app starts, it connects to a file called `app.db` in the same folder.
This file is a SQLite database — a lightweight database stored as a single file on disk.

Every time you add, update, or delete a flashcard, the change is written to `app.db`
immediately. When you close the app and reopen it, it reads from the same file.
Your flashcards are never stored in memory — they live on disk from the moment you save them.

If you want to reset all your data, simply delete `app.db`.
The app will create a fresh empty database the next time it runs.

# About Application

A simple terminal-based app for creating and studying flashcards.
All data is saved to a local file on your computer and stays there. Between sessions, close the app and reopen it, your cards are still there.

Built with pure Python 3. No external packages required.

## Features

- **Add** flashcards with a title, content, and optional tag
- **View** all saved flashcards in a clean list
- **Update** any flashcard — keep fields you like, change what you don't
- **Delete** flashcards with a confirmation step to prevent accidents
- **Search** across title, content, and tag with a single keyword
- **Random review** — get a surprise flashcard for a quick study session
- **Persistent storage** — data survives closing and reopening the app


## Tips

- Use **tags** to group related cards (e.g. `Python`, `Math`, `History`)
- Use **Search** to quickly find all cards with a specific tag or keyword
- Use **Random review** when you only have a minute to study
- The app will never crash on bad input — all fields are validated before saving