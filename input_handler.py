def user_move():
    while True:
        try:
            attack = int(input('enter 1 for punch, 2 for kick'))
            if attack == 1 or attack == 2:
                return attack
            else:
                print('please enter an attack')
        except ValueError:
            print('please enter an integer')
def user_defence():
    while True:
        try:
            defence = input('choose your defence: 1 for high, 2 for low : ')
            if defence == 1 or defence == 2:
                return int(defence)
            else:
                print('please enter a defence')
        except ValueError:
            print('please enter an integer')
