

correct_username = "admin"
correct_password = "helloadmin"


for i in range (3):
    username = input("Please enter username:")
    password = input("Please enter the password:")
    if username == correct_username and password == correct_password:
        print ("Welcome to the system,", username)
        break
else:
    print("Access denied!")