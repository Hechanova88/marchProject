#Welcomes the user alllowing proper i.d to access.
def intro():
  allowed_users = ['G', 'JOSEPPH', 'BERNARD']
  user = input("Welcome, please enter user I.D: ").upper()
#If user has correct i.d they will be prompted to lab3  
  if user in allowed_users:
    print(lab3())
  else:
    print("Invalid User, Try again")

#lab3 assingment
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
 
#run again funtion   
runAgain = "YES"
while runAgain == "YES":
  intro()
print("thanks").upper