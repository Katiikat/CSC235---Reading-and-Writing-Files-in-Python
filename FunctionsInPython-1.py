# My adventure game using Functions!


import random
from time import sleep

score = 0


# intro to set the story for the user
def display_intro_to_user(name):
    print("You wake up in your bed, a little groggy. Waking up to another day in quarantine.")
    print("You think to yourself \"What should I do today?\"")
    print("You roll over an look at your desk that's next to your bed.")
    print("Fully aware of all the schoolwork you should be doing, and the scholarships you should be applying for,"
          "you decide to get up and go downstairs.")
    print(f"Walking into the living room, your mother says \"Good morning {name}.\"")
    ans = input("Say it back? Yes or No\n").lower()
    # included for user interaction
    if ans == "yes":
        print("You say good morning to your mother and sit on the couch.")
        print("You pull your phone out and begin to play your favorite type of mobile games. Word Scrambles.")
    else:
        print("You smile at your mother and sit on the couch.")
        print("You pull your phone out and begin to play your favorite type of mobile games. Word Scrambles.")


# gather info about the user to be used in the story
def get_user_info():
    name = input("What is your first name?\n")
    display_intro_to_user(name)


# outline the rules of the mobile game
def word_scramble_intro():
    print("\n\nWelcome to Extreme Word Scramble.")
    print("On each level, you will have to solve a single scrambled word.")
    print("You will have 3 attempts to guess the word correctly.")
    print("Guess the word correctly, you will receive 5 points and a choice to move to the next level.")
    print("Use all your attempts and you will not receive any points, will not move on, and will not be able"
          "to repeat the level for 5 hours.")
    print("Good luck.\n\n")


# choose a word and scramble it for the user to then guess
def word_game_shuffle():
    word_scramble_intro()
    repeat = True

    # 10 total words in the word app game
    # todo: Read the words in from a text file??

    # words = ["scared", "hospital", "confined", "programming", "distract", "develop",
    # "practical", "required", "dictionary", "practice"]

    # opens file to retrieve words for the game
    get_words = open("words.txt", "r")

    words = []
    guessed = []
    for i in get_words:
        words.append(i.strip())

    while repeat:
        # select word to scramble from word list above
        word_to_scramble = words[random.randrange(0, 9)]
        if word_to_scramble in guessed:
            if len(words) == len(guessed):
                break

            continue
        guessed.append(word_to_scramble)
        # convert string into list
        scrambled_word_list = list(word_to_scramble)
        # shuffle list
        random.shuffle(scrambled_word_list)
        # convert list to string
        final_word = ''.join(scrambled_word_list)
        print("Your shuffled word is: ", final_word)
        repeat = guess_word(word_to_scramble)
    print(f"Your ending score was {score} out of {len(words) * 5}")
    return len(words) * 5


# user is given a chance to guess the word up to 3 times in total
def guess_word(word_to_scramble):
    global score
    tries = 3
    while tries > 0:
        guess = input("Type your guess here: ")
        guess = guess.upper()

        if guess == word_to_scramble.upper():
            print("Congratulations, you passed this level!")
            print("You gained 5 points.")
            score = score + 5
            print("Your new score: ", score)

            ans = input("Would you like to continue on? Y/N\n")
            ans = ans.upper()

            if ans == "N" or ans == "NO":
                return False

            return True
        else:
            print("Sadly, what you have entered is not correct.")
            tries = tries - 1
            print(f"You have {tries} more attempts.")

    # dialogue if the user uses all 3 attempts
    print("You are the weakest link... goodbye.\n")
    print("You throw you phone down on the couch, angrily, and decided to go do something productive with your life.")
    print("Like your homework... or laundry.\n")
    return False


# ending dialogue for the user.
def ending(full_score):
    if score == full_score:
        print("\n\nCongratulations on beating the game. Go and order yourself a cookie on your"
              "favorite food delivery service!")
        print("You smile at your phone as you conquered your favorite type of mobile game.")
        print("Looking up from your phone, you realize day has turned to evening.")
        print("You see a sandwich you mom set on the coffee table in front of you for lunch, just as she calls for"
              "dinner.")
        print("As your tummy grumbles out of hunger, you walk into the kitchen for dinner with your mom.")
        print("You think \"I'll do something productive tomorrow.\"")
        print("The end.")
    print("\n\nSince you are no longer playing the game, you sit and think of something to do.")
    print("After a while, you found something productive to do with your day and at dinner, "
          "you felt satisfied with the work you did.")
    print("You have a lovely dinner with your family and to their surprise, you offer to do the dishes before bed.")
    print("Perhaps you will try the game again tomorrow. Only time will tell.")
    print("You decide to send a text to your friend.")
    message = input("Type your message: ")

    # write message to file
    to_write = open("messages.txt", "w")
    to_write.write(message)

    print("Message Sent Successfully. Message Saved Successfully.")
    print("...")
    sleep(5)
    print("...")
    sleep(2)
    print("\"No response. He must be in bed.\" You follow and go lay in bed. Quickly, you dream about squirrels.")
    print("The end.")


# main class
print("\n\nBefore we begin...\n")
get_user_info()
max_score = word_game_shuffle()
ending(max_score)
