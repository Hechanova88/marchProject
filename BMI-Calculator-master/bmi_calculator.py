#introduction
def intro():
  allowed_users = ['G', 'JOSEPPH', 'BERNARD']
  user = input("enter user I.D: ").upper()
  
  if user in allowed_users:
    print(app())
  else:
    print("Invalid I.D")

def bmi():
  
  weight_in_lbs = float(input("How much do you weigh in lbs? "))
  height_in_ft = float(input("How tall are you in feet? "))


#imperial to metric weight   
  metric_weight = round((weight_in_lbs * 0.453592), 2)

#imperial to metric height
 
  height_metric = round((height_in_ft * 0.3048), 2)

  print("\nYour weight in kilograms is:", metric_weight)
  print("Your height in meters is:", height_metric)
  
  BMI = input("\nWould you like to know your BMI?")
  if BMI == "no":
    print(intro())
  else:
    user = metric_weight / (height_in_ft ** 2)
    userbmi = round((user * 10 + 2), 2)
  if userbmi <= 15.0:
    print("Your BMI is:", userbmi, "Severely Underweight!")
  elif 16.0 < userbmi <= 18.0:
    print("Your BMI is:", userbmi, "Underweight!")
  elif 18.0 < userbmi <= 25:
    print("Your BMI is:", userbmi, "Normal")
  elif 25.0 < userbmi <= 35.0:
    print("Your BMI is:", userbmi, "Overweight")
  else: 
    35.0 < userbmi <= 40.0
    print("Your BMI is:", userbmi, "Obese!")

def tip():

 print("\nWelcome to Tip Calculator!\n")

 bill = float(input("How much was dinner? "))

 percent_tip = float(input("What percentage tip do you want to give? "))

#calculate taxes    
 taxes = round((bill * 0.06), 2)

# calculate the tip
 tip = round((percent_tip / 100 * bill), 2)

#calculate the total bill plus tip
 total = round((bill + tip + taxes), 2)

 print("Your tip amount is: $", tip)

 print("Your total bill with sales tax is: $", total)

#number of split
 split = input('would you like to split?')
 if split == "yes":
    guests = int(input("How many people are in yout party?"))
    splitBill = total/guests
    print("Your new total is: $", splitBill)
    input("Run again: ")
 else:
    print("Your total bill with sales tax is: $", total)



def rock():
  print("Hello There!")
  name = input("What's your name?\n")
  print("Nice to meet you", name.title())
  print("Let's play a game")
  play = input("Would you like to play rock, paper, scissors with me?\n")
  while play == "yes": 
   from random import choice
   objects = ["rock", "paper", "scissors"]
   computer = choice(objects)
   rps = str(input("Rock, paper, or scissors? "))
   if rps == computer:
    print("I chose", computer)
    print("Well this is awkward. It's a tie")
    play = input("Would you like to play again?\n")
   if rps == ("rock"):
    if computer == ("scissors"):
      print("I chose", computer)
      print("You have bested me")
      play = input("Would you like to play again?\n")  
   if rps == ("paper"):
    if computer == ("rock"):
      print("I chose", computer)
      print("You have bested me")
      play = input("Would you like to play again?\n")
   if rps == ("rock"):
    if computer == ("scissors"):
      print("I chose", computer)
      print("You have bested me")
      play = input("Would you like to play again?\n")
   if computer == ("scissors"):
    if rps == ("paper"):
      print("I chose", computer)
      print("I win gg")
      play = input("Would you like to play again?\n")
   if computer == ("rock"):
    if rps == ("scissors"):
      print("I chose", computer)
      print("I win gg")
      play = input("Would you like to play again?\n")
   if computer == ("paper"):
    if rps == ("rock"):
      print("I chose", computer)
      print("I win gg")
      play = input("Would you like to play again?\n")
   else:
      print("Thanks for playing rock, paper, scissors!")


def lab3():
  myList =[]
  for i in range(0,10):
    number = float(input("Enter a list of 10 whole numbers: "))
#adds numbers to the list
    myList.append(number)
#sorts the list
    myList.sort()
#prints and removes duplicates
  print(set(myList))

def calculator():
 def add(x, y):
   
#adds two numbers
   return x + y
 def subtract(x, y):
#subtracts two numbers

   return x - y
 def multiply(x, y):

#multiplies two numbers
   return x * y
 def divide(x, y):
#divides two numbers
   return x / y

# take input from the user
 print("Select operation.")
 print("1.Add")
 print("2.Subtract")
 print("3.Multiply")
 print("4.Divide")

 choice = input("Enter choice(1/2/3/4):")

 num1 = int(input("Enter first number: "))
 num2 = int(input("Enter second number: "))

 if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

 elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

 elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

 elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
 else:
   print("Invalid input")


#guessing game
def guess():
   import random
#numbers are from 0 to 21
   randomNumber = random.randint(0, 21)
   count = 0

   while True:
        count += 1
        number = int(input('Enter the number between 0 to 20: '))
        if number < randomNumber:
            print('Too small')
        elif number > randomNumber:
            print('Too large')
        else:
            print('You have got it in', count, 'tries')
            break

 


runAgain = "YES"

#main menu selection
def app():
 app = input("\nWelcome! \n-Press 1 to calculate tip\n-Press 2 to calculate bmi\n-Press 3 for rock paper scissors\n-Press 4 for list\n-Press 5 for calculator\n-Press 6 for number guessing game\n")
 if app == "1":
    print(tip())
 if app == "2":
    print(bmi())
 if app == "3":
    print(rock())
 if app == "4":
   print(lab3())
 if app == "5":
  print(calculator())
 if app == "6":
  print(guess())


#run again 
while runAgain == "YES":
  intro()
print("thanks").upper
