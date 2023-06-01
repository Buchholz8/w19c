#this function will while loop waiting for the try statement which will set attack = to a user input
#the if will check what attack they chose and return it
#the exception makes sure its a number
#the defence function is basically the same thing
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
