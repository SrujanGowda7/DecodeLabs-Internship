print("=" * 55)
print("      AI Recommendation System")
print("=" * 55)

# Dataset
recommendations = {
    "movies": {
        "action": ["Avengers", "John Wick", "Mad Max", "Mission Impossible"],
        "comedy": ["3 Idiots", "The Mask", "Jumanji", "Free Guy"],
        "sci-fi": ["Interstellar", "Inception", "The Matrix", "Avatar"]
    },

    "books": {
        "fiction": ["Harry Potter", "The Alchemist", "The Hobbit"],
        "technology": ["Python Crash Course", "Clean Code", "AI Basics"],
        "self-help": ["Atomic Habits", "Deep Work", "Think and Grow Rich"]
    },

    "music": {
        "pop": ["Blinding Lights", "Perfect", "Levitating"],
        "rock": ["Numb", "Believer", "Bohemian Rhapsody"],
        "classical": ["Moonlight Sonata", "Four Seasons", "Canon in D"]
    }
}

while True:

    print("\nChoose a category")
    print("1. Movies")
    print("2. Books")
    print("3. Music")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "4":
        print("\nThank you for using the AI Recommendation System!")
        break

    elif choice == "1":
        print("\nMovie Genres")
        print("Action | Comedy | Sci-Fi")
        genre = input("Enter genre: ").lower()

        if genre in recommendations["movies"]:
            print("\nRecommended Movies:")
            for movie in recommendations["movies"][genre]:
                print("•", movie)
        else:
            print("Genre not available.")

    elif choice == "2":
        print("\nBook Categories")
        print("Fiction | Technology | Self-Help")
        genre = input("Enter category: ").lower()

        if genre in recommendations["books"]:
            print("\nRecommended Books:")
            for book in recommendations["books"][genre]:
                print("•", book)
        else:
            print("Category not available.")

    elif choice == "3":
        print("\nMusic Categories")
        print("Pop | Rock | Classical")
        genre = input("Enter category: ").lower()

        if genre in recommendations["music"]:
            print("\nRecommended Songs:")
            for song in recommendations["music"][genre]:
                print("•", song)
        else:
            print("Category not available.")

    else:
        print("Invalid choice. Please try again.")