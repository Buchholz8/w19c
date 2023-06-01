from input_handler import user_defence, user_move
import random

user_health = 100
computer_health = 100
attack_input = user_move
defense_input = user_defence
computer_attack = 'punch' if random.randint(0, 100) < 50 else 'kick'
computer_defense = 'high' if random.randint(0, 100) < 50 else 'low'
while user_health > 0 and computer_health > 0:
    print('User Health:', user_health)
    print('Computer Health:', computer_health)
    print()

    if attack_input == 1 and computer_defense == 'low':
        print('User hits the computer!')
        computer_health -= 10
    elif attack_input == 2 and computer_defense == 'high':
        print('User hits the computer!')
        computer_health -= 10
    elif computer_attack == "punch" and defense_input == 2:
        print('Computer hits the user!')
        user_health -= 10
    elif computer_attack == "kick" and defense_input == 1:
        print('Computer hits the user!')
        user_health -= 10

    print()

if user_health <= 0:
    print('Computer wins!')
elif computer_health <= 0:
    print('User wins!')