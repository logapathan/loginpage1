db_username="ram"
db_password="12345"

for i in range(3):
    username = input("Enter Your Username:")
    password = input("Enter Your Password:")
    if username==db_username and password==db_password:
        print("Login sucessful")
        break
    elif username!=db_username and password!=db_password and i==2:
        print("Too many incorrect attempt!!! Try Again after 5 minutes")
        break
    else:
        print("Incorrect username or password!!! Try Again")
        continue








