import secrets

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
    
    words = ["python", "developer", "programming", "algorithm", "hardware", 
             "software", "robotics", "compiler", "processor"]
             
    word = secrets.choice(words)  
    guessed_word = ["_"] * len(word) 
    attempts = 6
    guessed_letters = set()
    
    while attempts > 0 and "_" in guessed_word:
        print("\nWord to guess:", " ".join(guessed_word))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
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






elif category == 1:
    print("You have selected, Mathematics")
    print("Try to guess the word. You have 6 incorrect guesses.")
  
   words = ["calculus", "theorem", "equation", "algebra", "probability", "geometry"]

    word = secrets.choice(words)  
    guessed_word = ["_"] * len(word) 
    attempts = 6
    guessed_letters = set()

    while attempts > 0 and "_" in guessed_word:
        print("\nWord to guess:", " ".join(guessed_word))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
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
        print("\nGame over! The word was:", word

 




elif category == 2:
    print("You have selected, science")
    print("Try to guess the word. You have 6 incorrect guesses.")

    words = ["molecule", "gravity", "chemistry", "genetics", "photosynthesis", 
             "biodiversity", "chromosome", "radiation"]

    word = secrets.choice(words)  
    guessed_word = ["_"] * len(word) 
    attempts = 6
    guessed_letters = set()

    while attempts > 0 and "_" in guessed_word:
        print("\nWord to guess:", " ".join(guessed_word))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
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
    




elif category == 3:
    print("You have selected, English")
    print("Try to guess the word. You have 6 incorrect guesses.")
    
words = ["grammar", "adjective", "onomatopoeia", "homophones", "prepositional", "hyperbole", "connotation"]

  word = secret.choice(words) 
    guessed_word = ["_"] * len(word) 
    attempts = 6
    guessed_letters = set() 
    
    while attempts > 0 and "_" in guessed_word: 
        print("\nWord to guess:", " ".join(guessed_word))
        guess = inout("Guess a letter: ").lower()
        
        if guess in guessed_letters: 
            print("You already guessed that letter. 
        elif guess in word: 
            guessed_letters.add(guess)
            print("You already guessed that letter. Try again.") 
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
        
        
elif category == 4:
    print("You have selected, History")
    print("Try to guess the word. You have 6 incorrect guesses.")

words = ["civilization", "colonization", "revolution", "archaeology", "imperialism"]

  word = secrets.choice(words)  
    guessed_word = ["_"] * len(word) 
    attempts = 6
    guessed_letters = set()
    
    while attempts > 0 and "_" in guessed_word:
        print("\nWord to guess:", " ".join(guessed_word))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
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
