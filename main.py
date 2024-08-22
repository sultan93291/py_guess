from random import randint

chance=5
computer_ran_num = randint(1,10)

def guess_number(guess_number, computer_ran_num , chance ):
    
    if(guess_number==computer_ran_num and chance >0):
      print("well,you guessed the number")
      return True
    
    else:
      print(f"you guessed the wrong number . ")
      return False

while chance > 0:
  user_inp_num = int(input("guess the number : "))

  if guess_number(user_inp_num, computer_ran_num,chance):
    break 
  chance-=1
  print(f"avilable chance : {chance}")

if(chance==0):
  print(f"oops you lose the game . best luck next time . chance left {chance}")
else:
  chance-=1
  print(f"you won the game the game . chance left {chance}")
  