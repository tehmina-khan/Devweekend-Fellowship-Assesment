## 1. How to Run

Make sure Python 3 is installed, then run:

py main.py OR python3 main.py 

That's the whole setup. There's nothing to install, no virtual environment needed, no `.env` file to configure. The first time it runs, the app creates `app.db` automatically in the same folder. From there the menu guides you through everything.

If you're on Windows and `python3` doesn't work, try `python` instead — same thing, just depends on how Python was installed. (Which I have also mentioned earlier, I provided 2 options fpr running the main file.)


## 2. Stack Choice

I went with Python and SQLite for two reasons: simplicity and fit.

Python's `sqlite3` module is built into the language, so the whole project runs with zero installs. That felt right for a CLI app of this size — pulling in an ORM or a separate database process would've been overkill.

SQLite specifically was a good fit because persistence was a core requirement.
Storing data in a JSON file or a plain text file would've worked for a prototype, but you'd have to load the whole file into memory every time and write your own search logic. SQLite gives you real queries, safe writes, and the data just sits in `app.db` without you thinking about it. It also means the database file is portable, it can be copied to another machine and all the flashcards move with it.

I kept `db.py` and `main.py` as separate files on purpose. `db.py` handles all the SQL, `main.py` handles the user interaction. Mixing them together would've made both files harder to follow.


## 3. One Real Edge Case

The one that needed the most thought was invalid flashcard IDs on update and delete.

If a user types an ID that doesn't exist, two things could happen silently:
the UPDATE or DELETE query runs, affects zero rows, and nothing breaks, but nothing happens either. The user gets no feedback and has no idea why their change didn't take effect.

The FIX was adding a `flashcard_exists(id)` function in `db.py` that does a lightweight lookup before any destructive operation. If the ID isn't there, `main.py` prints a clear message and returns to the menu early. The user knows immediately that the ID was wrong, rather than assuming the app broke.

It's a small thing but it's the kind of bug that would frustrate someone actually using the app day-to-day.


## 4. AI Usage

I used ChatGPT during the planning phase — mostly to talk through the folder
structure and think about how to split responsibilities between `db.py` and
`main.py`. It also helped me draft sections of the README faster than I would
have done from scratch.

For the code itself, some AI-suggested snippets were a bit over-engineered, more abstraction than a project this size needed. I rewrote those parts manually to make them easier to follow. Things like flattening nested logic, using plain `if/elif` instead of class hierarchies, and keeping helper functions short enough to read without scrolling. The goal was code a first-year student could pick up and understand without a guided tour.

In general I treated the AI suggestions as a starting point to react to, not a finished answer to copy.


## 5. Honest Gap

The biggest gap is the CLI navigation experience.

Right now, if you're halfway through updating a flashcard and change your mind, there's no way to cancel, you either complete the flow or you leave a partial edit. A proper "press 0 to go back" option at each step would make the app feel a lot more solid.

Validation is also fairly basic. The app prevents blank titles and catches non-numeric IDs, but it doesn't cap input length or handle unusual characters.

For a flashcard app that's probably fine, but if the content field accepted formatted text or the tags became searchable categories, you'd want stricter rules there.

These aren't hard problems, I just started the assignment late due to some other commitments. If this were going to real users I'd tackle the navigation first.
