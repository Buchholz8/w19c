from input_handler import user_defence, user_move
import random
#i import random for the computer number and i imported the user_defence and user_move functions from input_handler
user_health = 100
computer_health = 100
#i set the values for the healths
while user_health > 0 and computer_health > 0:
    print('User Health:', user_health)
    print('Computer Health:', computer_health)
    print()
#this while loop doesnt work and im not sure why, this will spam my console with these prints and wont let me choose any moves
    attack_input = user_move
    defense_input = user_defence
#i set the player attack and defence values
    if attack_input is None or defense_input is None:
        continue
#i tried to fix the while loop issue with this buyt it didnt work, i wanted to leave it here to see your opinion on this logic
    computer_attack = 'punch' if random.randint(0, 100) < 50 else 'kick'
    computer_defense = 'high' if random.randint(0, 100) < 50 else 'low'
#i set the computers attack and defence based off of random.randint
    if attack_input == 1 and computer_defense == 'low':
        print('User hits the computer!')
        computer_health -= 10
    elif attack_input == 2 and computer_defense == 'high':
        print('User hits the computer!')
        computer_health -= 10
    elif computer_attack == 'punch' and defense_input == 2:
        print('Computer hits the user!')
        user_health -= 10
    elif computer_attack == 'kick' and defense_input == 1:
        print('Computer hits the user!')
        user_health -= 10
#this if-elif will just go through the user input and computer inputs to see their results and will - 10 off the opposing hp based off the result
    print()
#i then print that
if user_health <= 0:
    print('Computer wins!')
elif computer_health <= 0:
    print('User wins!')
#this if-elif is a game checker to see if any of their hps reach 0 or below 

#not sure why this just loops and prints the healths i tried taking that out of the loop and just post it before
#and just making it set the value and update it that way but then my console just looped through nothing just a blank console
#so i tried to google and couldnt find a reason