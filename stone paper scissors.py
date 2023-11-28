import random
def get_user_choice():
    user_choice=input("choose rock,paper,scissors(or type 'quit'to end):").lower()
    if user_choice=='quit':
        return user_choice
    if user_choice not in ["rock","paper","scissors"]:
        print("invalid choice.please choose rock ,paper,scissors.")
        return get_user_choice()
    return user_choice
def get_computer_choice():
    return random.choice(["rock","paper","scissors"])
def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "its a tie"
    if((user_choice=="rock" and computer_choice=="scissors")or(user_choice=="paper" and computer_choice=="rock")or( user_choice=="scissors" or computer_choice=="paper")):
        return "you win"
    else:
        return "computer wins"
while True:
    user_choice=get_user_choice()
    if user_choice=='quit':
        break
    computer_choice=get_computer_choice()
    print(f"the computer choose{computer_choice}")
    result=determine_winner(user_choice,computer_choice)
    print(result)
print("thanks for playing")    
