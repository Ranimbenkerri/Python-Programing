from random import randint


true_number = randint(1, 100)
print(true_number)
easy = 10
hard = 5

def true(guess, number):
    
    if guess > number:
        return "too high"
    elif guess < number:
        return "too low"
    else:
        return "YOU WIN"
    
def end_game(q):
    q=True 
       

print("welcome to the number Guessing Game ")
user = input("choose a difficulty . Type 'easy' or 'hard' : ")

if user == 'easy':
    a = 10
if user == 'hard':
    a = 5
    
    
q = False

user_number = 0
while user_number != true_number and a>0 :
    print(f"you have {int(a)} attempts")
    user_number = int(input("Make a guess: "))
    print(true(int(user_number), int(true_number)))
    a=a-1
 
if user_number != true_number:
    print(f"You lose , the right number is {true_number}")