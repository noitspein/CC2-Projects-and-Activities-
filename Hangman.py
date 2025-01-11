
print("Welcome to Hangman!")
print("Categories:")
print("0 - Technology")
print("1 - Mathematics")
print("2 - Science")
print("3 - English")
print("4 - History")

category = int(input("Select a category: "))

if category == 0:
    print("You have selected, Technology")
    print("Try to guess the word. You have 6 incorrect guesses.")
    
    import secrets
    
    words = ["python", "developer", "programming", "algorithm", "hardware", "software", "robotics", "compiler", "processor"]
    
    random_word = secrets.choice(words)
  
    guess = input("Guess a letter: ")
    
    
    
    
    











elif category == 1:
    print("You have selected, Mathematics")
    print("Try to guess the word. You have 6 incorrect guesses.")
    
elif category == 2:
    print("You have selected, Science")
    print("Try to guess the word. You have 6 incorrect guesses.")
    
elif category == 3:
    print("You have selected, English")
    print("Try to guess the word. You have 6 incorrect guesses.")
    
elif category == 4:
    print("You have selected, History")
    print("Try to guess the word. You have 6 incorrect guesses.")
    
else:
    print("Category is out of range"]





















    print("Welcome to Hangman!")
    print("Categories:")
    print("0 - Technology")
    print("1 - Mathematics")
    print("2 - Science")
    print("3 - English")
    print("4 - History")

 elif category = int(input("Select a category: "))
        0: ["python", "developer", "programming", "algorithm", "hardware", "software", "robotics", "compiler", "processor"],
        1: ["algebra", "geometry", "calculus", "equation", "matrix", "fraction", "variable", "angle"],
        2: ["gravity", "molecule", "biology", "physics", "chemistry", "evolution", "experiment", "element"],
        3: ["grammar", "adjective", "sentence", "vocabulary", "language", "prose", "poetry", "rhyme"],
        4: ["revolution", "empire", "dynasty", "medieval", "warfare", "treaty", "civilization", "monarch"]
    }

    if category not in word_lists:
        print("Category is out of range.")
        return

    print(f"You have selected category {category}. Try to guess the word. You have 6 incorrect guesses.")

    words = word_lists[category]
    random_word = secrets.choice(words)

    guessed_word = ["_"] * len(random_word)  # Blanks for the word
    attempts = 6
    guessed_letters = []

    while attempts > 0 and "_" in guessed_word:
        print("\nWord:", " ".join(guessed_word))  # Display blanks or guessed letters
        print(f"Remaining attempts: {attempts}")
        print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")
        guess = input("Guess a letter: ").lower()

        if len(guess) = 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in random_word:
            print("Correct!")
            for i, letter in enumerate(random_word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print("Incorrect!")
            attempts -= 1

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", random_word)
    else:
        print("\nOut of attempts! The word was:", random_word)

