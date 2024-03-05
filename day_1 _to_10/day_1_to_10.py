import random
import math

# print("welcome to the tip calculator.")
# totalBill = float(input("what was the total bill?"))
# tipAmount = int(input("What percentage would you like to tip?"))
# numberGuests= int(input("How many people to split the bill?"))
# finalAmount= round((totalBill * (1 + tipAmount/100))/numberGuests, 2)

# print(f"${finalAmount}" )

# print(random.randint(1, 100) + random.random())
# print(random.random())
# states_of_america = ["Delaware", "Florida"]
# dictionary = { 
#     123: "First_record",
#     345: "third_record"
#     }

# print(dictionary)

#####Hangman####

# list_of_words = ["Legion", "Mustard", "Mayonaise", "Ketchup"]

# def pick_random_word():
#     selected = random.choice(list_of_words).lower()
#     return selected

# #pick a random world from list
# selected_word = pick_random_word()
# print(selected_word)


# #calculate player's life count
# player_life_count = len(selected_word)

# # display blanks
# list = []

# for _ in range(len(selected_word)):
#     list += "_"

# print(list)

# end_of_game = False

# while not end_of_game:
#     player_guess = input("Guess a letter in this word:\n").lower()
     
    
#     if selected_word.find(player_guess) <= 0:
#         player_life_count -= 1
#         print(f"WRONG! player points value: {player_life_count}")

#     for position in range(len(selected_word)):
#         letter = selected_word[position]
#         if player_guess == letter:
#             list[position] = letter
#             print(f"player points value: {player_life_count}")
    
#     if player_life_count == 0:
#         end_of_game = True

#     if "_" not in list:
#         end_of_game = True
#         print("You win!!")

#     print(list)

# math module. math.ceil(), math.floor()

##### check for prime numbers ####
# def check_for_prime(number):
#     is_prime = True

#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False

#     if is_prime:
#         print("This is a prime number")
#     else:
#         print("Not a prime number")

# number = int(input("Provide a number: \n"))
# check_for_prime(number)