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

