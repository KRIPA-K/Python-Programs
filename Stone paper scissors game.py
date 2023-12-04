name = input("Hey give me your name " )
text_prompt = "Hey" +name+ "How many rounds would you like to play ?"
flag = True
def take_rounds_input():
    while True:
        rounds = int(input(text_prompt))
        if rounds%2 == 1:
            print('Wow its an odd')
            if rounds > 2 and rounds < 10:
                print('we got perfect odd number')
                break
            else:
                print('your number is not in the range of 3 to 9, please enter again')
        else:
            print("Its and even, enter again")
import random
def give_me_a_computer_choice():
    option_list = ('rock','paper','scissors')
    return random.choice(option_list)
def give_me_player_option():
    option = input("R= Rock, P= Paper, S= Scissors")
    if option == 'R' or option == 'r':
        return 'rock'
    elif option == 'P' or option == 'p':
        return 'paper'
    elif option == 'S' or option == 's':
        return 'scissors'
    else:
        return give_me_player_option()
def check_who_is_winning(computer_input,player_input):
    if player_input == 'scissors' and computer_input =='scissors':
        return 'draw'
    elif player_input == 'rock' and computer_input =='scissors':
        return 'player'
    elif player_input == 'paper' and computer_input =='scissors':
        return 'computer'
    elif player_input == 'scissors' and computer_input =='rock':
        return 'computer'
    elif player_input == 'rock' and computer_input =='rock':
        return 'draw'
    elif player_input == 'paper' and computer_input =='rock':
        return 'player'
    elif player_input == 'scissors' and computer_input =='paper':
        return 'player'
    elif player_input == 'rock' and computer_input =='paper':
        return 'computer'
    elif player_input == 'paper' and computer_input =='paper':
        return 'draw'
    else:
        return "Some error is there in spellings"
lst=[]
lst.append('draw')
lst.append('player')
lst.append('player')
def check_ultimate_winner(round_list):
    player = round_list.count('player')
    computer= round_list.count('computer')
    draw=round_list.count('draw')
    if player > computer:
        return "player"
    elif computer > player:
        return "computer"
    else:
        return "draw"
    

             
