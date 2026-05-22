import db

# DISPLAY HELPeRS
def print_line():
    print("  " + "─" * 46)


def print_header(title):
    print()
    print(f"  ── {title} ──")
    print_line()


def print_flashcard(card):
   
    print_line()
    print(f"  ID      : {card['id']}")
    print(f"  Title   : {card['title']}")
    print(f"  Content : {card['content']}")
    print(f"  Tag     : {card['tag'] if card['tag'] else '(none)'}")
    print(f"  Created : {card['created_at']}")
    print_line()


def print_cards_list(cards):
    
    if not cards:
        print("\n  (No flashcards to show.)\n")
        return

    for card in cards:
        print_flashcard(card)


# INPUT HELPERS STARTS FROM HERE

def ask_required(prompt):

    while True:
        value = input(prompt).strip()
        if value:
            return value
        # .strip() means "   " (spaces only) is also treated as empty
        print("  ⚠  This field is required. Please enter a value.")


def ask_optional(prompt):

    value = input(prompt).strip()
    return value if value else None


def ask_id(prompt):

    while True:
        raw = input(prompt).strip()
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("  ⚠  Please enter a valid ID (a positive whole number).")


# FEATURE FUNCTIONS LISTING

def add_flashcard():
    print_header("ADD FLASHCARD")

    title   = ask_required("  Title   : ")
    content = ask_required("  Content : ")
    tag     = ask_optional("  Tag     : (press Enter to skip) ")

    db.add_flashcard(title, content, tag)

    print("\n  ✅  Flashcard saved!\n")


def view_all_flashcards():
    print_header("ALL FLASHCARDS")

    cards = db.get_all_flashcards()

    if not cards:
        print("\n  No flashcards yet. Add one with option 1!\n")
        return

    print(f"\n  {len(cards)} flashcard(s):\n")
    print_cards_list(cards)


def update_flashcard():

    print_header("UPDATE FLASHCARD")

    flashcard_id = ask_id("  Enter the ID to update: ")

    # Checks if ID exists 
    if not db.flashcard_exists(flashcard_id):
        print(f"\n  ⚠  No flashcard found with ID {flashcard_id}.\n")
        return

    # Fetch only desired card 
    current = db.get_flashcard_by_id(flashcard_id)

    print(f"\n  Editing flashcard #{flashcard_id}")
    print("  Press Enter on any field to keep the current value.\n")

    # Display the existing value in brackets 
    raw_title   = input(f"  Title   [{current['title']}]: ").strip()
    raw_content = input(f"  Content [{current['content']}]: ").strip()
    raw_tag     = input(f"  Tag     [{current['tag'] if current['tag'] else 'none'}]: ").strip()

    # Empty input Logic
    new_title   = raw_title   if raw_title   else current["title"]
    new_content = raw_content if raw_content else current["content"]
    new_tag     = raw_tag     if raw_tag     else current["tag"]

    db.update_flashcard(flashcard_id, new_title, new_content, new_tag)

    print("\n  ✅  Flashcard updated!\n")


def delete_flashcard():
   
    print_header("DELETE FLASHCARD")

    flashcard_id = ask_id("  Enter the ID to delete: ")

    if not db.flashcard_exists(flashcard_id):
        print(f"\n  ⚠  No flashcard found with ID {flashcard_id}.\n")
        return

    current = db.get_flashcard_by_id(flashcard_id)
    print(f"\n  You are about to permanently delete:")
    print(f"  \"{current['title']}\"")
    print()

    confirm = input("  Type 'yes' to confirm: ").strip().lower()

    if confirm == "yes":
        db.delete_flashcard(flashcard_id)
        print("\n  ✅  Flashcard deleted.\n")
    else:
        print("\n  Cancelled — nothing was deleted.\n")


def search_flashcards():
    print_header("SEARCH FLASHCARDS")

    keyword = ask_required("  Keyword : ")

    results = db.search_flashcards(keyword)

    if not results:
        print(f"\n  No flashcards matched '{keyword}'.\n")
        return

    print(f"\n  Found {len(results)} result(s) for '{keyword}':\n")
    print_cards_list(results)


def review_random():

    print_header("RANDOM REVIEW")

    card = db.get_random_flashcard()

    if card is None:
        print("\n  No flashcards yet — add some with option 1!\n")
        return

    print("\n  Here is your random flashcard:\n")
    print_flashcard(card)
    print()


# MENU SECTIOn

def show_menu():
    print()
    print("  +------------------------------------------------+")
    print("  |         Flashcard Study App                    |")
    print("  +------------------------------------------------+")
    print("  |  1.  Add flashcard                             |")
    print("  |  2.  View all flashcards                       |")
    print("  |  3.  Update flashcard                          |")
    print("  |  4.  Delete flashcard                          |")
    print("  |  5.  Search flashcards                         |")
    print("  |  6.  Review random flashcard                   |")
    print("  |  7.  Exit                                      |")
    print("  +------------------------------------------------+")


MENU_ACTIONS = {
    "1": add_flashcard,
    "2": view_all_flashcards,
    "3": update_flashcard,
    "4": delete_flashcard,
    "5": search_flashcards,
    "6": review_random,
}


# MAIN LOOP

def run():

    db.create_table()  
    print("\n  Welcome to Flashcard Study App!")

    while True:
        show_menu()

        choice = input("\n  Choose an option (1-7): ").strip()

        if choice == "7":
            print("\n  Goodbye! Keep studying!\n")
            break  #the program ends here

        elif choice in MENU_ACTIONS:
            MENU_ACTIONS[choice]()  # This Callx the matching feature function

        else:
            print("\n  ⚠  Invalid choice. Please enter a number between 1 and 7.\n")


if __name__ == "__main__":
    run()
