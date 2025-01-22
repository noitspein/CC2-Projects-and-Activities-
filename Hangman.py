import secrets

print(
    "Welcome to Hangman!\n"
    "Categories:\n"
    "0 - Technology\n"
    "1 - Mathematics\n"
    "2 - Science\n"
    "3 - English\n"
    "4 - History"
)

category = int(input("Select a category: "))

category_names = ["Technology", "Mathematics", "Science", "English", "History"]
category_words = {
    0: ["python", "developer", "programming", "algorithm", "hardware", "software", "robotics", "compiler", "processor"],
    1: ["calculus", "theorem", "equation", "algebra", "probability", "geometry"],
    2: ["molecule", "gravity", "chemistry", "genetics", "photosynthesis", "biodiversity", "chromosome", "radiation"],
    3: ["grammar", "adjective", "onomatopoeia", "homophones", "prepositional", "hyperbole", "connotation"],
    4: ["civilization", "colonization", "revolution", "archaeology", "imperialism"]
}

if category in category_words:
    print(f"You have selected, {category_names[category]}. Try to guess the word. You have 6 incorrect guesses.")

    words = category_words[category]
    word = secrets.choice(words)
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()

    while attempts > 0 and "_" in guessed_word:
        print("\nWord to guess:", " ".join(guessed_word))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            print("Guessed letters so far:", ", ".join(sorted(guessed_letters)))
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Correct! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print(f"Incorrect! '{guess}' is not in the word. Attempts left: {attempts}")

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame over! The word was:", word)
else:
    print("Invalid category. Please restart the game.")
    
def main():
    while True:
        play_game() 
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        
        if play_again != "no":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()