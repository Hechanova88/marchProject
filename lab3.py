allowed_users = ['G', 'JOSEPPH', 'BERNARD']
user = input("enter: ").upper() 
if user in allowed_users:
    print(app())
else:
    print("Try again")